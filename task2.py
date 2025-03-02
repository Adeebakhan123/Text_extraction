from pickle import HIGHEST_PROTOCOL
from PIL import Image, ImageOps, ImageFilter,ImageDraw
import os

def print_pixel_values(image_path):
   image = Image.open(image_path)
   img=image.convert('L')
   pixels=img.load()
   width, height = image.size
   #print(width,height)
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
                    #print(pixels[y,x])
                    if pixels[y-1,x]==255 and pixels[y+1,x]==255:
                       pixels[y,x]=255 
        
   
   return img
   




# Call the function with the path to your image

if not os.path.exists("results"):
    os.makedirs("results")

for i in range(10):
    path_to_image = os.path.join(os.getcwd(), "images", "image_{0}.png".format(i))
    imge_new= print_pixel_values(path_to_image)
    #imge_new.show()
    imge_new.save(path_to_image.replace("images", "results"))
    
    
    
       
