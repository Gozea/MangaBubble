# Finetuning Tesseract for custom font

This folder is dedicated to finetune Tesseract for OCR. Finetuning Tesseract is only useful if you have some custom font. Otherwise, it's probably recommended to skip this step as the model you will finetune will be slower than the fast checkpoints optimized for time cost efficiency.

This folder mainly contains :

- config.ini
- tesseract_train.sh

### Configuration

Before executing the script, you should modify the variables in config.ini :

- modify _base\_model_ to download the checkpoint of the language you want (you can find the list [here](https://github.com/tesseract-ocr/langdata_lstm/tree/main))
- modify _new\_model_ to name your finetuned model however you want
- modify _text\_files_ to download the necessary files to generate the training data (you can find the list [here](https://github.com/tesseract-ocr/tessdata_best)) 
- modify _font_ if you have the URL to a custom font

### Execute 

You can do the finetune with this command in this directory

```chmod a+x *.sh && ./tesseract_train.sh```

You will be asked if you want to generate training data before executing the training
