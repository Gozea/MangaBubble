# get text files from config
text_files=$(awk '/text_files/ { print $3 }')
font=$(awk '/font/ {print $3}')

# download the unicharset and training text
wget -qq "https://raw.githubusercontent.com/tesseract-ocr/langdata_lstm/main/" + $text_files + "/" + $text_files + ".unicharset"
wget -qq "https://raw.githubusercontent.com/tesseract-ocr/langdata_lstm/main/" + $text_files + "/" + $text_files + ".training_text"

# optional files
wget -qq "https://raw.githubusercontent.com/tesseract-ocr/langdata_lstm/main/" + $text_files + "/" + $text_files + ".numbers"
wget -qq "https://raw.githubusercontent.com/tesseract-ocr/langdata_lstm/main/" + $text_files + "/" + $text_files + ".punc"
wget -qq "https://raw.githubusercontent.com/tesseract-ocr/langdata_lstm/main/" + $text_files + "/" + $text_files + ".wordlist"

# download font 
wget $font
