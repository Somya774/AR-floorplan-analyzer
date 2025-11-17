let scene, camera, renderer, controls, mesh;

initScene();

function initScene() {
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111111);

  const width = window.innerWidth, height = window.innerHeight;
  camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 2000);
  camera.position.set(0, 150, 300);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(width, height);
  document.body.appendChild(renderer.domElement);

  // ✅ OrbitControls now works in r128
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;

  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(100, 200, 100);
  scene.add(light, new THREE.AmbientLight(0xffffff, 0.6));

  animate();
}

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

document.getElementById('generate').onclick = async () => {
  const fileInput = document.getElementById('fileInput');
  if (!fileInput.files.length) return alert("Please select an image.");
  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  const response = await fetch("/upload", {
    method: "POST",
    body: formData,
  });

  const blob = await response.blob();
  const img = await createImageBitmap(blob);
  create3DFromDepth(img);
};

function create3DFromDepth(img) {
  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");
  const size = 256;
  canvas.width = size;
  canvas.height = size;
  ctx.drawImage(img, 0, 0, size, size);
  const data = ctx.getImageData(0, 0, size, size).data;

  const geometry = new THREE.PlaneGeometry(300, 300, size - 1, size - 1);
  const pos = geometry.attributes.position;
  for (let i = 0; i < size * size; i++) {
    const brightness = data[i * 4];
    const z = (brightness / 255) * 100 - 50;
    pos.setZ(i, z);
  }
  pos.needsUpdate = true;
  geometry.computeVertexNormals();

  const texture = new THREE.CanvasTexture(canvas);
  const material = new THREE.MeshStandardMaterial({ map: texture, side: THREE.DoubleSide });

  if (mesh) {
    scene.remove(mesh);
    mesh.geometry.dispose();
    mesh.material.dispose();
  }
  mesh = new THREE.Mesh(geometry, material);
  mesh.rotation.x = -Math.PI / 2;
  scene.add(mesh);
}
