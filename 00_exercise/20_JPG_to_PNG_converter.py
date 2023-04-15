import os
from sys import argv
from os import path, makedirs, listdir
from PIL import Image

input_dir = argv[1]
output_dir = argv[2]

if path.isdir(input_dir) is False:
    print("Input directory is invalid. Try again")
else:
    if path.exists(output_dir) is False:
        print(f"Creating directory {output_dir}")
        makedirs(output_dir)
        print(f"Created new directory {output_dir}")

    for file_img in listdir(input_dir):
        curr_file = Image.open(f"{input_dir}{file_img}")
        clean_name = path.splitext(file_img)[0]
        curr_file.save(f"{output_dir}{clean_name}.png", "png")
        print(f"copied {file_img}")

    print("All done!")
