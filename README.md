# Manga Bubbles

This repository is a project for automatic translation of Manga pages. The pipeline is the following :

Detect texts in the pages using _YOLOv8_ -> Execute OCR on the detected texts using _Tesseract_ -> Translate the texts using _mBART_

The project was primarly designed for this task but you can also use the folders to finetune the models I used for you own tasks. Just go to the folder you want, modify its config.ini then execute the bash scripts that has the name of its corresponding folder (the README in each folder will guide you)

![Alt image](imgs/bocchi_boxes.png =200x200)

<div>
    <img src="imgs/translated_box.png" width="48%">
    <img src="imgs/deepl.png" width="48%" >
</div>

### Requirements

You will need python3 and pip to use this repository. You can install all the requirements with this command :

```pip install -r requirements.txt```

### Execute

To execute this repository, you can use the bash script :

```chmod a+x manga_bubbles.sh && ./manga_bubbles```

The script will guide you whether you want to finetune the different models further, then will execute the python file _manga_bubbles.py_

The repository comes with an exemple image _bocchi.jpg_ but you can also add you own image to this repo, then modify the config.ini file to apply the pipeline on it (you only have to change the variable _image_ to the name of you image)
