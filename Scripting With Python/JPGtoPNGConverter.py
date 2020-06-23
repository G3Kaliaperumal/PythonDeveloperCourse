import sys
import os
from PIL import Image

# Fetch the folder names via command line arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

cwd = os.path.abspath(os.getcwd())

is_output_folder_exists = os.path.isdir(output_folder)
if not is_output_folder_exists:
    mode = 0o777
    path = os.path.join(cwd, output_folder)
    os.mkdir(path, mode)

is_image_folder_exists = os.path.isdir(image_folder)
if is_image_folder_exists:
    path = os.path.join(cwd, image_folder)
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            new_image_path = os.path.join(cwd, output_folder)
            image = Image.open(f'{path}\\{filename}')
            image.save(
                f'{new_image_path}\\{os.path.splitext(filename)[0]}.png', 'png')
else:
    print('Oops! No such folder exists')
