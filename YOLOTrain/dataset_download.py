import os, shutil
import yaml
import configparser

from roboflow import Roboflow


# get the api key in the config file
configparser = configparser.ConfigParser()
configparser.read("./config.ini")
api_key = configparser["KEYS"]["API_KEY"]


# download dataset in the colab session
rf = Roboflow(api_key=api_key)
project = rf.workspace("temp-lulqc").project("manga-text-detect")
dataset = project.version(3).download("yolov8")


# create dataset folder
shutil.move("Manga-Text-Detect-3", "./datasets/Manga-Text-Detect-3")


# modify the yaml file
yaml_file = "./datasets/Manga-Text-Detect-3/data.yaml"
with open(yaml_file, 'r') as f:
    data = yaml.safe_load(f)

    # Iterate through each key-value pair in the YAML data
    for key, value in data.items():
        # Check if the key starts with "train" or "eval"
        if key.startswith('train') :
            data[key] = "./train/images"
        if key.startswith('val') :
            data[key] = "./valid/images"

# Write the modified data back to the YAML file
with open(yaml_file, 'w') as f:
    yaml.dump(data, f)
