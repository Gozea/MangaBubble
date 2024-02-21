from ultralytics import YOLO

"""# Train YOLO for box detection

We're using a dataset from Roboflow to train a bubble detection model by finetuning a YOLOv8 model.
Please use your own API key after creating your account to download this dataset (! the dataset has NSFW content !) or feel free to use your own dataset
"""

# !!! you need to rewrite train and val path in the data.yaml file !!!
model = YOLO('yolov8n.pt')
results = model.train(data="./datasets/Manga-Text-Detect-3/data.yaml", epochs=3)

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
print(f"boxmap : {metrics.box.map}")    # map50-95
print(f"map50 : {metrics.box.map50}")  # map50
print(f"map75: {metrics.box.map75}")  # map75
