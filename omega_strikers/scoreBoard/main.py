### Purpose is to extract the information from the end of game scoreboard.
### Use Opitcal Character Recognition (OCR) libraries to detect and extract text. - pytesseract

### It might be helpful to preprocess the image... cropping.. perhaps, if the locations are fixed,
### I could take the original screenshot and output many different images of each 'field'

import pytesseract
from PIL import Image

# Tesseract-OCR executable location downloaded from https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
original_image = Image.open('omega_strikers/scoreBoard/scorebrd.png')

list_left = (790, 790, 790, 790, 790, 790, )
list_upper = (390, 445, 495, 620, 673, 725, )
list_right = (960, 960, 960, 960, 960, 960, )
list_lower = (425, 475, 529, 665, 707, 759, )

import itertools

list_names = list()

for (left, upper, right, lower) in zip(list_left, list_upper, list_right, list_lower):
   left = left
   upper = upper
   right = right
   lower = lower
   cropped_image = original_image.crop((left, upper, right, lower))
   cropped_image.show()
   text = pytesseract.image_to_string(cropped_image)
   list_names.append(text)