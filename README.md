# 🚗💤 Driver Drowsiness Detection System (YOLOv8)

> **An end‑to‑end, real‑time AI system that detects driver fatigue using deep learning, computer vision, and temporal reasoning.**
> Built from scratch — dataset → training → deployment → realtime decision logic.

---

## 🔥 Project Overview

Driver drowsiness is one of the **leading causes of road accidents worldwide**. Human fatigue cannot be reliably monitored with traditional sensors alone. This project introduces a **vision‑based, real‑time Driver Drowsiness Detection System** that continuously monitors eye and mouth behavior to infer alertness.

This is **not just an object detection model** — it is a **complete AI system** combining:

* Deep learning–based perception (YOLOv8)
* Temporal reasoning (time‑based logic)
* Real‑time deployment (webcam inference)

---

## 🎯 Key Objectives

* Detect facial cues related to fatigue (eye closure, yawning)
* Track these cues **over time**, not frame‑by‑frame
* Classify driver state as **ALERT** or **DROWSY** in real time
* Run efficiently on **consumer‑grade hardware**

---

## 🧠 System Intelligence (Why This Is Different)

Most academic demos stop at *"eye closed detected"*.
This system goes further:

* ❌ Single‑frame predictions are ignored
* ✅ **Temporal consistency** is enforced
* ✅ Prolonged eye closure triggers fatigue
* ✅ Repeated yawning escalates risk
* ✅ Real‑time feedback is provided to the driver

This mirrors how **production safety systems** are designed.

---

## 🏗️ Architecture Overview

```
Camera Feed
   ↓
YOLOv8m Object Detector
   ↓
Eye / Mouth State Detection
   ↓
Temporal Logic Engine
   ↓
Driver State Classification
(ALERT / DROWSY)
   ↓
Realtime Visual Feedback
```

---

## 📦 Dataset Details

* **Total Images:** ~16,000

* **Annotation Type:** Bounding boxes

* **Classes (11):**

  * Attentive eye
  * Drowsy eye
  * Eyeclosed
  * Open‑Mouth
  * Yawn / noYawn
  * open / closed
  * asleep

* **Source:** Roboflow Universe

* **License:** CC BY 4.0

The dataset focuses on **fine‑grained facial states**, making it challenging and highly realistic.

---

## 🧪 Data Pipeline

* Image resizing and normalization
* Bounding box validation
* Data augmentation (color jitter, blur, grayscale, CLAHE)
* Train / Validation split

All preprocessing is compatible with **YOLOv8 training standards**.

---

## 🤖 Model Details

* **Model:** YOLOv8m (Medium)
* **Parameters:** ~25.8M
* **Backbone:** CSP‑based CNN with feature pyramid
* **Input Resolution:** 768 × 768
* **Framework:** Ultralytics YOLO (PyTorch)

Chosen deliberately to balance:

* Accuracy on small facial features
* Realtime performance
* Limited GPU availability (Colab Free)

---

## ⚙️ Training Strategy

* **Platform:** Google Colab (Free GPU)
* **GPU:** NVIDIA Tesla T4
* **Epochs:** ~20 (early stopping based on validation performance)
* **Optimizer:** AdamW
* **Mixed Precision:** Enabled (AMP)

### 📈 Performance Highlights

* **mAP@50:** ~0.50
* **Recall:** ~0.80+
* **Stable convergence** with no divergence or collapse

Early stopping was applied following **professional ML practice**, prioritizing generalization over overfitting.

---

## 🎥 Realtime Inference (Core Feature)

The trained model is deployed locally for **live webcam inference**.

### Capabilities:

* Detects eye and mouth states frame‑by‑frame
* Aggregates predictions over time
* Outputs real‑time driver status

```text
ALERT   → Normal blinking and behavior
DROWSY  → Prolonged eye closure or yawning
```

---

## 🧠 Temporal Drowsiness Logic

This project’s **key differentiator** is the decision logic layer.

### Logic Rules:

* Eye closed for > 2 seconds → **DROWSY**
* Repeated yawning → **DROWSY**
* Normal blinking → **ALERT**

This removes false positives caused by:

* Blinking
* Head movement
* Lighting variation

---

## 🖥️ Local Deployment

The system runs locally using:

* Python
* OpenCV
* Ultralytics YOLO

```bash
yolo detect predict model=best.pt source=0
```

No cloud dependency — suitable for **edge deployment**.

---

## 🧪 Testing Scenarios

✔ Normal driving posture → ALERT
✔ Eyes closed > 2s → DROWSY
✔ Yawning → DROWSY
✔ Continuous monitoring without lag

The system performs reliably under real‑world conditions.

---

## 🚀 Potential Applications

* Driver assistance systems (ADAS)
* Fleet safety monitoring
* Commercial vehicle fatigue alerts
* Edge AI / embedded vision systems
* Research in human‑state recognition

---

## 🛣️ Future Enhancements

* 🔊 Audio alarm integration
* 📊 Fatigue scoring over time
* 👥 Multi‑person detection
* 🚘 In‑vehicle camera integration
* 🧠 Transformer‑based temporal modeling

---

## 🧑‍💻 Tech Stack

* **Language:** Python
* **Deep Learning:** PyTorch
* **Model:** YOLOv8 (Ultralytics)
* **Computer Vision:** OpenCV
* **Training:** Google Colab (GPU)
* **Deployment:** Local realtime webcam

---

## 🏆 Why This Project Matters

This project demonstrates:

* End‑to‑end ML system design
* Practical deployment skills
* Engineering trade‑offs under constraints
* Real‑world problem solving with AI

> **This is not a toy demo — it is a deployable, real‑time AI safety system.**

---

## 📜 License

This project is released for educational and research purposes.
Dataset license follows **CC BY 4.0**.

---

## 🙌 Acknowledgements

* Ultralytics YOLO
* Roboflow Universe
* Open‑source ML community

---

🚀 *Built with an engineer’s mindset — from data to deployment.*
