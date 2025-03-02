from pytesseract import pytesseract
from PIL import Image
import os
path_to_tesseract= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd =path_to_tesseract

if not os.path.exists("texts"):
    os.makedirs("texts")
def print_text(image):
    newimage = Image.open(image)
    text = pytesseract.image_to_string(newimage)
    return text



for i in range(10):
    path_to_image = os.path.join(os.getcwd(), "results", "image_{0}.png".format(i))

    text= print_text(path_to_image)
    print (text)
    

