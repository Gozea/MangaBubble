import os, subprocess, configparser

import pytesseract


# get data from config file
config = configparser.ConfigParser()
config.read("config.ini")
text_files = config["texts"]["text_files"]
new_model = config["models"]["new_model"]

# parameters
training_text_file = f'{text_files}.training_text'
output_directory = f'{new_model}-ground-truth'
font = "Noto Sans JP"

# create new folder
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# scrap each line and create one-line files
line_max=100
with open(training_text_file, 'r') as input_file:
    for idx, line in enumerate(tqdm(input_file.readlines())):
         if idx < line_max:
            line_training_text = os.path.join(output_directory, f'gt_{idx}.gt.txt')
            with open(line_training_text, 'w') as output_file:
                output_file.writelines([line])

            # apply text2image on the one-line file
            subprocess.run(['text2image',
                    f'--text=./{line_training_text}',
                    f'--outputbase={output_directory}/gt_{idx}',
                    f'--font={font}',
                    '--fonts_dir=./',
                    '--writing_mode=vertical-upright',
                    '--strip_unrenderable_words',
                    '--xsize=2000',
                    '--ysize=2000',
                    '--char_spacing=1.0',
                    '--leading=32',
                    '--exposure=0',
                    f'--unicharset_file=./{text_files}.unicharset'
            ])
