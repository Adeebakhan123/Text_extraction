import tkinter as tk
from tkinter import NONE, filedialog
from types import NoneType
from PIL import ImageTk, Image,ImageOps, ImageFilter,ImageDraw
from pickle import HIGHEST_PROTOCOL
import os
from pytesseract import pytesseract
root = tk.Tk()
tesseract_path=""
def path_tesseract():
    global tesseract_path
    tesseract_path = filedialog.askopenfilename(filetypes=[("exe file", "*.exe")],
        title="Select an Executable File")

    if tesseract_path:
        pytesseract.tesseract_cmd = tesseract_path
        tesseract_label.config(text=f"Selected file: {tesseract_path}")
        result_label.config(text="")
        open_button.config(state="normal")
    else:
        result_label.config(text="Somthing went wrong \n Tesseract path is required.")
        open_button.config(state="disabled")
    
# Define a function to open a file dialog and get the image file

def open_image():
    if tesseract_path is None:
        result_label.config(text="Tesseract path is not set. Please set it first.")
        return
    file_path = filedialog.askopenfilename(filetypes=[("png file", "*.png")],
        title="Select an Executable File")
    if file_path:
        try:
            image = Image.open(file_path)
            image1=image
            photo = ImageTk.PhotoImage(image)
   
        
            
        
    #image to cleaned image 
            img=image1.convert('L')
            pixels=img.load()
            width, height = image1.size
            for y in range(height):
                for x in range(width):
                   pixel_color=img.getpixel((x,y))
                   if pixel_color>120:
                     pixel_color=255
                   else:
                     pixel_color=0

                   pixels[x,y]=pixel_color 
            for x in range(width):
                for y in range(1,height-1):
                    if pixels[x,y]==0:
                        if pixels[x,y-1]==255 and pixels[x,y+1]==255:
                            pixels[x,y]=255
            for x in range(height):
                for y in range(1,width-1):
                    if pixels[y,x]==0:
                        if pixels[y-1,x]==255 and pixels[y+1,x]==255:
                            pixels[y,x]=255 
            cleaned_image=img 
            cleaned_photo = ImageTk.PhotoImage(cleaned_image)
            
        #extract text from the image
            extracted_text = pytesseract.image_to_string(cleaned_image)
            image_label.config(image=photo)
            image_label.image= photo # type: ignore
            cleaned_label.config(image=cleaned_photo)
            cleaned_label.image = cleaned_photo     # type: ignore
            text_label.config(text=extracted_text)
        except:
            image_label.config(text="something went wrong please select correct path")
            return
def clear_display():
    image_label.config(image=None) #type: ignore
    image_label.image= None    # type: ignore
    cleaned_label.config(image=None)  # type: ignore
    cleaned_label.image= None  # type: ignore
    text_label.config(text="")
   
# Styling for labels and buttons
label_style = ("Helvetica", 14)
button_style = ("Helvetica", 12, "bold")
# Label and entry for Tesseract path input
tesseract_label = tk.Label(root, text="Text extraction:",font=label_style)
tesseract_label.pack()  

# Create a button to open the file dialog 
open_button=tk.Button(root,text="Select tesseract Ocr path",command=path_tesseract,font=button_style)

open_button.pack()

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_image,font=button_style)
open_button.pack()
#disable the open image button by default
open_button.config(state="disabled")
# Create a label to display the selected image
image_label = tk.Label(root)
image_label.pack()
# Create a label to display the cleaned image
cleaned_label = tk.Label(root)
cleaned_label.pack()
#Create a lable1 to display
text_label = tk.Label(root, wraplength=400, justify="right",font=("Helvetica", 12))
text_label.pack()

clear_button = tk.Button(root, text="Clear", command=clear_display,)
clear_button.pack()


result_label = tk.Label(root, wraplength=400, justify="left")
result_label.pack()


root.mainloop()

   
   
        
   

   










