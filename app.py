from flask import Flask, render_template, request, send_file, abort
import torch
import cv2
import numpy as np
import os 
from PIL import Image
import io

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Load MiDaS 
print("Loading MiDaS model...")
# model "MiDaS_small"
model_name = "MiDaS_small"  
midas = torch.hub.load("intel-isl/MiDaS", model_name)
midas.to(device).eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_name == "MiDaS_small":
    transform = midas_transforms.small_transform
else:
    transform = midas_transforms.dpt_transform

print("MiDaS loaded. Model:", model_name)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400

    f = request.files["image"]
    filename = f.filename or "upload.jpg"
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)

    try:
        depth = generate_depth(path)
    except Exception as e:
        # log and return error
        print("Error during depth generation:", e)
        return {"error": str(e)}, 500

    # Normalize depth 
    depth_norm = (depth - depth.min()) / (depth.max() - depth.min() + 1e-8)
    depth_img = (depth_norm * 255.0).astype(np.uint8)

    # Encode to PNG in-memory
    is_success, buffer = cv2.imencode(".png", depth_img)
    if not is_success:
        return {"error": "Failed to encode depth image"}, 500
    io_buf = io.BytesIO(buffer.tobytes())
    io_buf.seek(0)
    return send_file(io_buf, mimetype="image/png")

def generate_depth(image_path):
    """Return a numpy 2D depth array (H x W) for the given image path."""
    
    pil_img = Image.open(image_path).convert("RGB")

    
    
    try:
        
        sample = transform(pil_img)
    except TypeError:
        
        np_img = np.asarray(pil_img)
        sample = transform(np_img)

    
    if isinstance(sample, dict):
        
        input_tensor = sample.get("image")
    else:
        input_tensor = sample

    # ensure tensor exists
    if input_tensor is None:
        raise RuntimeError("Transform did not return a valid tensor.")

    # Put batch dim and device
    if len(input_tensor.shape) == 3:
        input_batch = input_tensor.unsqueeze(0).to(device)
    elif len(input_tensor.shape) == 4:
        input_batch = input_tensor.to(device)
    else:
        raise RuntimeError("Unexpected tensor shape from transform: " + str(input_tensor.shape))

    # Inference
    with torch.no_grad():
        prediction = midas(input_batch)
        
        if prediction.dim() == 4:
            prediction = prediction.squeeze(1)
        pred = prediction.cpu().numpy()[0]

        
        orig_w, orig_h = pil_img.size
        pred_resized = cv2.resize(pred, (orig_w, orig_h), interpolation=cv2.INTER_CUBIC)

    return pred_resized

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True)
