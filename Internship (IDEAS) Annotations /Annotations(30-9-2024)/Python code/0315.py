import json
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the JSON annotation file
json_path = "/mnt/data/project-4-at-2025-04-10-10-16-afb7523d.json"
image_path = "/mnt/data/DJI_0315.JPG"

with open(json_path, "r") as file:
    data = json.load(file)

# Load the image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extract annotations related to DJI_0315.JPG
annotations = [item for item in data if item.get("image") == "DJI_0315.JPG"]

# Overlay annotations
for annotation in annotations:
    for region in annotation.get("annotations", []):
        for result in region.get("result", []):
            if result["type"] == "polygon":
                points = np.array([(p["x"] * image.shape[1] / 100, 
                                    p["y"] * image.shape[0] / 100) 
                                   for p in result["value"]["points"]], np.int32)
                points = points.reshape((-1, 1, 2))
                cv2.polylines(image, [points], isClosed=True, color=(255, 0, 0), thickness=2)

# Display the image with annotations
plt.figure(figsize=(10, 8))
plt.imshow(image)
plt.axis("off")
plt.show()
