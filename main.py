
""" 16/10/2022 - Felipe V Assunção """

from rembg import remove
from PIL import Image

input_path = 'C:/Users/felip/Desktop/RemoveBackgrounImage/img.jpg' # input image path
output_path = 'C:/Users/felip/Desktop/RemoveBackgrounImage/img.png' # output image path

input = Image.open(input_path) # load image
output = remove(input) # remove background
output.save(output_path) # save image

