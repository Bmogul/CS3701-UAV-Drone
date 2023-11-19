import cv2
import scipy
from ultralytics import YOLO

model = YOLO("yolov8s.pt")

results = model.train(data='config.yaml', epochs=3, device='mps')
