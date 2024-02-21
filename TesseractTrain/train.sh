# save current location
current_location=$(pwd)

# config file
base_model=$(awk '/base_model/ { print $3}')
new_model=$(awk '/new_model/ { print $3}')
text_files=$(awk '/text_files/ { print $3}')

# output directory
output_directory=$new_model + "-ground-truth"

# get tesstrain to get the tesseract training utilities
git clone https://github.com/tesseract-ocr/tesstrain

pip install -r tesstrain/requirements.txt --quiet
cd tesstrain && make tesseract-langdata && make leptonica tesseract

# move the ground truth in tesstrain
mv $output_directory "tesstrain/data/" + $output_directory

# download checkpoint
# checkpoint needs to be moved in the data/tessdata folder for training
wget "https://github.com/tesseract-ocr/tessdata_best/raw/main/" + $base_model + ".traineddata"
mkdir tesstrain/data/tessdata && mv $base_model + ".traineddata" "tesstrain/data/tessdata/" + $base_model + ".traineddata"

# move optional files in tesseract folder
mkdir "tesstrain/data/" + $new_model
mv -t "tesstrain/data/" + $new_model + "/" $text_files + ".numbers" $text_files + ".punc" $text_files + ".wordlist"


# execute training
# Make sure to check the list of variables in the Train section in the readme of tesstrain (you can also use the command "make help")
echo "Begin Training"
make training MODEL_NAME=$new_model\ START_MODEL=$base_model\ TESSDATA=data/tessdata PSM=5 MAX_ITERATIONS=100

# copy the .traineddata in the current location
cd $current
cp tesstrain/data/{new_model}.traineddata .
