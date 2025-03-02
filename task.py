from PIL import Image, ImageOps, ImageFilter,ImageDraw
import os
def print_pixel_values(image_path):
   image = Image.open(image_path)
   img=image.convert('L')
   pixels=img.load()
   width, height = image.size

   for y in range(height):
        for x in range(width):
            pixel_color=img.getpixel((x,y))
            if pixel_color>120:
                pixel_color=255
                

            else:
                pixel_color=0

            pixels[x,y]=pixel_color   
        #remove_horizontal_lines()  
   #img.show()  
   return img
   

def get_cleared_from_image(image_path):
 
# Open the image


# Load the image
 image = Image.open(image_path)
 image.show()

# Convert the image to grayscale
 bw_image = ImageOps.grayscale(image)

# Apply thresholding to create a binary image
 threshold_value = 128  # Adjust this value as needed
 binary_image =bw_image.point(lambda p: p > threshold_value and 255)

# Use morphological operations to remove horizontal lines
 kernel = ImageFilter.Kernel((3, 3), [0, 0, 0, 1, 1, 1, 0, 0, 0])  # 3x3 kernel with ones in the center row
 cleaned_image = binary_image.filter(kernel)

# Save or display the final cleaned image

 cleaned_image.show()


 #cleaned_image.show()
 return cleaned_image


# Call the function with the path to your image

if not os.path.exists("results"):
    os.makedirs("results")

for i in range(10):
    
    path_to_image = os.path.join(os.getcwd(), "images", "image_{0}.png".format(i))
    img_new=print_pixel_values(path_to_image)
    img_new.show()
    image = get_cleared_from_image(img_new)
    image.show()
    image.save(path_to_image.replace("images", "results"))
    