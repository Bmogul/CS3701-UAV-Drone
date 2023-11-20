import cv2
import scipy
from ultralytics import YOLO
import os

model = YOLO("yolov5s.pt")
results = model.train(data='config.yaml', epochs=3, device='mps')

# video_paths = ["./videos/drone1DroneTracking1.mp4", "./videos/drone2DroneTracking2.mp4"]
videos_path = "./videos"
output_path = "./detections"

for video in os.listdir(videos_path):
    video_path = os.path.join(videos_path, video)

    if os.path.isfile(video_path):
        print()
        detectFolder = os.path.join(output_path, video) 
        video_capture = cv2.VideoCapture(video_path)
        os.makedirs(detectFolder, exist_ok=True)
        # frame_number = 0
        frames = []
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frames.append(frame)
            # frame_number += 1
            # print(f"Frame {frame}")
            results = model(frames)
            for i, result in enumerate(results):
                if result.boxes is not None and len(result.boxes.xyxy) > i and len(result.boxes.xyxy[i]) > 0:
                    for box in result.boxes.xyxy[i]:
                        x1, y1, x2, y2 = map(int, box)
                        cv2.rectangle(frames[i], (x1, y1), (x2, y2), (0, 255, 0), 2)

                    cv2.imwrite(f"{detectFolder}/{i}.jpg", frames[i])

video_capture.release()


