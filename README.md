# pothole-detection-yolov8
# 🚧 Pothole Detection using YOLOv8 + Streamlit

A complete end-to-end **Object Detection** project that detects **potholes on roads** using **YOLOv8** and provides a simple **Streamlit web app** for inference.

 Live App: https://pothole-detection5.streamlit.app/

---

##  Project Highlights
-  Trained **YOLOv8** object detection model for pothole detection
-  Dataset verified (label-image match + bounding box visualization)
-  Notebook-based training + evaluation
-  Streamlit web app for easy image upload and detection
-  Confidence threshold slider to control false positives vs missed detections

---

##  Model Performance (Validation)
Object detection is evaluated using **mAP**, not classification accuracy.

| Metric | Score |
|------|------|
| Precision (P) | **0.865** |
| Recall (R) | **0.67** |
| mAP@50 | **0.789** |
| mAP@50–95 | **0.503** |

> Notes:
> - **mAP@50** = overall detection quality at IoU=0.50  
> - **mAP@50–95** = stricter metric averaged over IoU thresholds (0.50 → 0.95)

---

##  How the App Works
1. Upload a road image (jpg/png/jpeg)
2. Adjust confidence threshold (default 0.25)
3. Model predicts pothole bounding boxes
4. Annotated image is displayed instantly

---

##  Tech Stack
- **YOLOv8 (Ultralytics)**
- **Python**
- **Streamlit**
- OpenCV / Pillow / NumPy

---

##  Project Structure
pothole-detection-yolov8/
├─ app.py
├─ requirements.txt
├─ packages.txt
└─ model/
└─ best.pt


---

##  Run Locally
### 1) Clone the repo
```bash
git clone https://github.com/<your-username>/pothole-detection-yolov8.git
cd pothole-detection-yolov8

pip install -r requirements.txt
streamlit run app.py
