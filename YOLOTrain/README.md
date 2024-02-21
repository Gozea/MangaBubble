# YOLOv8 for bubble detection

This folder is dedicated to the YOLOv8 model. This folder should mainly contain :

- yolov8n.pt : the current last checkpoint to the YOLOv8 model
- yolo_train.sh : execute all the python files to finetune YOLOv8

### Finetuning YOLOv8

You can finetune the model if you 're not satisfied with the current accuracy of the model. You only have to execute the yolo.sh file 

```chmod a+x yolo.sh && ./yolo.sh```

Doing so will ask you if you want to download the Manga-Detect-3 dataset using the Roboflow API (you will have to create [an account](https://roboflow.com/)) by using your Roboflow API key. Be aware that the dataset used by default has NSFW content.

### Finetuning using a custom dataset

You can also finetune a YOLOv8 model using your custom dataset instead of the Manga-Detect-3 but you will have to modify directly the code in dataset_download.py. Please create a folder named datasets here and place your dataset there.

```mkdir datasets```

Your custom dataset has to contains the bounding boxes in the right format for a YOLOv8 model and must contain a data.yaml file. You can create your own dataset with its annotations in the right format using [Roboflow](https://roboflow.com/) (please check the documentation).
