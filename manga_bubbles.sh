read -p "Do you wish to first finetune models ? [Y/N]" answer

yolo_dir=$(awk '/yolo_dir/ { print $3 }' config.ini}
tesseract_dir=$(awk '/tesseract_dir/ { print $3 }' config.ini}
mbart_dir=$(awk '/mbart_dir/ { print $3 }' config.ini}

if [ "$answer" = "Y" || "$answer" = "y"]; then
    read -p "Do you wish to finetune the YOLO model ?" answer
    if [ "$answer" = "Y" || "$answer" = "y"]; then
        echo "Begin YOLO train" 
        ./$yolo_dir\/yolo_train
    fi
    read -p "Do you wish to finetune the tesseract model ?" answer
    if [ "$answer" = "Y" || "$answer" = "y"]; then
        echo "Begin tesseract train" 
        ./$tesseract_dir\/tesseract_train
    fi
    read -p "Do you wish to finetune the mBART model ?" answer
    if [ "$answer" = "Y" || "$answer" = "y"]; then
        echo "Begin mBART train" 
        ./$mbart_dir\/mbart_train
    fi
    echo "End of finetuning"
fi

echo "Executing manga_bubble"
python3 manga_bubble.py
