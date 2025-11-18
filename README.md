🏠 AR-FloorPlan-Prototype
2D Floor Plan → 3D AR Visualization (Web-Based Architecture Tool)

AR-FloorPlan-Prototype is a web-based system that converts 2D architectural floor plans into interactive 3D models and visualizes them in Augmented Reality (WebXR).
Built using Computer Vision + 3D Graphics + AR, this project demonstrates strong technical proficiency across OpenCV.js, Three.js, WebGL, and WebXR.

This project is designed to help architects, designers, and clients better understand spatial layouts by experiencing them at real-world scale.

## ⭐ Why This Project Matters 

Demonstrates end-to-end problem solving using CV + 3D + AR.

Fully browser-based, no app installation required.

Showcases skills in image processing, mesh generation, AR rendering, and modern JavaScript workflows.

Real-world use case for architecture, real estate, interior design, and educational demos.

## 🚀 Key Features

Upload a 2D floor-plan image

Automated edge + contour detection using OpenCV

Converts layout into 3D wall structures

Real-time AR placement via WebXR

Explore model through rotate, walk-around, zoom

Lightweight and mobile-friendly

🛠 Tech Stack

Frontend: HTML, CSS, JavaScript
Computer Vision: OpenCV.js
3D Rendering: Three.js (WebGL)
AR: WebXR API
Tools: VS Code, local server, npm utilities

## Tools & Technologies Used — AR Floorplan Analyzer
🔹 Programming Languages

Python (image processing & backend logic)

C# (Unity scripting)

Java / Kotlin (ARCore dependencies for Android build, if applicable)

🔹 Frameworks & Engines

Unity 3D (core engine for AR rendering)

Unity AR Foundation (cross-platform AR functionality)

ARCore (Google) (tracking, plane detection, AR environment)

🔹 Image Processing & Conversion

OpenCV (Python) – for:

Floorplan contour detection

Edge detection

Shape extraction

Room segmentation

Pillow (PIL) – for image handling and preprocessing.

🔹 3D Generation & Modeling

Unity Mesh API (for generating 3D meshes from contours)

ProBuilder (optional) (for manual adjustments or mesh refinement)

Blender (optional) (if used for any model cleanup)

🔹 Build & Deployment Tools

Android SDK (for building APK)

Unity Hub (project management)

Gradle (Unity Android builds)

🔹 File Formats & Integration

  PNG / JPEG – input floorplan images

JSON – passing extracted layout coordinates to Unity

OBJ / FBX (optional) – for 3D layout export

🔹 Additional Tools 

Git / GitHub – version control

VS Code / PyCharm – Python development

Visual Studio / Rider – Unity C# scripting

## 📂 Project Structure
AR-FloorPlan-Prototype/
│── index.html
│── app.js
│── style.css
│── assets/
│── screenshots/   ← Add your screenshots here
│── README.md

3D Rendering: Three.js (WebGL)🧠 How It Works

Floor-plan image uploaded

OpenCV processes edges + contours

Walls extruded into 3D

Scene rendered using Three.js

WebXR places model in AR for real-scale viewing

## 📌 Future Scope

AI-based room segmentation

Window/door recognition

Multi-floor support

Material + texture rendering

Export to GLB/OBJ
AR: WebXR API
Tools: VS Code, local server, npm utilities

## 👤 Author
Somya  Agerawal

B.Tech CSE | Computer Vision & AI | AR/VR Projects | Data Science Enthusiast

Skilled in CV, ML, WebXR, and modern JS

Building real-world interactive prototypes

Passionate about immersive tech & intelligent systems
