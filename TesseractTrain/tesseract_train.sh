# Generate text files ?
read -p "Do you need to generate text files" answer

if [ "$answer" = "Y" || "$answer" = "y" ]; then
    echo "Begin downloading necessary files for generation..."
    ./download_texts_files.sh
    echo "Generating texts"
    python3 generate_texts.py
fi

# tesstrain
echo "Preparing Tesstrain"
./train.sh
