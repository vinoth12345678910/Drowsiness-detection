import cv2
import time
from ultralytics import YOLO

model = YOLO("best.pt")

EYE_CLOSED_TIME = 2.0
eye_closed_start = None

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4, verbose=False)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detections.append(label)

    status = "ALERT"

    if "Eyeclosed" in detections or "Drowsy eye" in detections:
        if eye_closed_start is None:
            eye_closed_start = time.time()
        elif time.time() - eye_closed_start > EYE_CLOSED_TIME:
            status = "DROWSY"
    else:
        eye_closed_start = None

    if "Yawn" in detections:
        status = "DROWSY"

    color = (0, 0, 255) if status == "DROWSY" else (0, 255, 0)

    cv2.putText(frame, status, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
