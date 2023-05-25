
import cv2
import numpy as np
import serial
import time

model = cv2.dnn.readNetFromDarknet('yolov4_custom.cfg', 'yolov4_custom_last.weights')
classes = ['can', 'glass', 'plastic', 'vinyl']

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
color = (255, 255, 255)

while True:
    ret, frame = cap.read()
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    model.setInput(blob)
    output = model.forward()

    class_ids = []
    confidences = []
    boxes = []
    for det in output:
        scores = det[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(det[0] * width)
            center_y = int(det[1] * height)
            w = int(det[2] * width)
            h = int(det[3] * height)
            x = center_x - w // 2
            y = center_y - h // 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in indices:
        i = i[0]
        box = boxes[i]
        x, y, w, h = box
        label = str(classes[class_ids[i]])
        color = (0, 255, 0) if label == 'can' else (0, 0, 255) if label == 'glass' else (255, 0, 0) if label == 'plastic' else (0, 255, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-5), font, font_scale, color, 2)

    cv2.imshow('object detection', frame)

cap.release()
cv2.destroyAllWindows()
