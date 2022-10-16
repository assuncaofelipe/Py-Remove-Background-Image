
""" 16/10/2022 - Felipe V Assunção """

from rembg import remove
from PIL import Image

input_path = 'C:/Users/user/Desktop/folder/name_file' # input image path - change path for your path
output_path = 'C:/Users/user/Desktop/folder/img.png' # output image path

input = Image.open(input_path) # load image
output = remove(input) # remove background
output.save(output_path) # save image

