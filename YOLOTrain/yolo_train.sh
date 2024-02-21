# Download the Dataset ?
read -p "Do you want to download the dataset using the Roboflow API ? (Y/N): " answer
# Convert the answer to uppercase for case-insensitive comparison
answer_uppercase=$(echo "$answer" | tr '[:lower:]' '[:upper:]')
if [ "$answer_uppercase" = "Y" ]; then
    # Need to update config file ?
    read -p "Do you need to update your API key ? (Y/N): " answer
    # Convert the answer to uppercase for case-insensitive comparison
    answer_uppercase=$(echo "$answer" | tr '[:lower:]' '[:upper:]')

    if [ "$answer_uppercase" = "Y" ]; then
        python3 input_api_key.py
    fi

    # Download using the Roboflow API 
    python3 dataset_download.py
fi


# Train the model
python3 yolo_train.py
