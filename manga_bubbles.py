# -*- coding: utf-8 -*-
import configparser
from PIL import Image, ImageDraw, ImageChops

from ultralytics import YOLO

import pytesseract

import torch
import accelerate
import transformers
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import preprocess


# configuration
config = configparser.ConfigParser()
config.read("config.ini")
models = config["models"]

# local path
img = Image.open(config["image"]["image"]).convert('L')

# yolo
yolo = YOLO(models["yolo_dir"] + "/" + models["yolo_model"])
predict_boxes = yolo(img)

# crops
boxes = []
for box in predict_boxes[0].boxes.xyxy:
    boxes.append(img.crop(box.cpu().numpy()))

# tesseract
tessconfig = f'-l {models["tesseract_model"]} --tessdata-dir {models["tesseract_dir"]}'
texts = []
for box in boxes:
    texts.append(pytesseract.image_to_string(clean_box(box), config=tessconfig))

#clean texts
clean_texts = [clean_tesseract(text) for text in texts]

# mBART
model_checkpoint = models["mbart_dir"] + "/" + models["mbart_model"]
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
# translation
tokenized_texts = tokenizer(clean_texts, padding=True, truncation=True, return_tensors='pt')
out = model.generate(**tokenized_texts, max_new_tokens=40, decoder_start_token_id=tokenizer.lang_code_to_id[config["languages"]["target_code"]])
translations = tokenizer.batch_decode(out, skip_special_tokens=True)

for id in range(len(translations)):
    print(f"box {id}")
    print(clean_texts[id])
    print(translations[id])

