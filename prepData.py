import cv2
import scipy
import os
import numpy as np


folder_path = './image_label'

for folder in os.listdir(folder_path):
    folder_full_path = os.path.join(folder_path, folder)

    if os.path.isdir(folder_full_path):
        annotation_file_path = os.path.join(folder_full_path, 'anotation.mat')
        if(os.path.exists(annotation_file_path)):
            print(f"Contents of 'anotaion.mat' in {folder}")

            data = scipy.io.loadmat(annotation_file_path)
            annotations = data['box']
            num = -1
            for i, annotation in enumerate(annotations, start=1):
                num+=1
                # Assuming each annotation has format [x_center, y_center, width, height]
                x_center, y_center, width, height = annotation

                # Get image dimensions to normalize coordinates
                image_path = os.path.join(folder_full_path, f"{num}0.jpg")  # Assuming image files are named 1.jpg, 2.jpg, ...
                if os.path.exists(image_path):
                    if(image_path == './image_label/5/730.jpg'):
                        print(num)
                    img = cv2.imread(image_path)
                    img_height, img_width, _ = img.shape

                    # Convert bounding box to YOLO format
                    x_center_norm = x_center / img_width
                    y_center_norm = y_center / img_height
                    width_norm = width / img_width
                    height_norm = height / img_height

                    # Print or use the converted coordinates for further processing
                    # print(f"Image {i}0.jpg: x_center={x_center_norm}, y_center={y_center_norm}, width={width_norm}, height={height_norm}")
                    yolo_annotation = f"0 {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n"  # Assuming '0' represents the class 'drone'
                    annotation_file_yolo = os.path.join(folder_full_path, f"{num}0.txt")  # YOLO annotation file path
                    with open(annotation_file_yolo, 'w') as f:
                        f.write(yolo_annotation)
                else:
                    i-=1  # If image file is missing, skip this annotation and move on to the next one
        else:
            print("No annotation file found in {folder}")