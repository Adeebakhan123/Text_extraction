import os
import cv2

def get_cleared_from_image(image_path):
    pass


if not os.path.exists("results"):
    os.makedirs("results")

for i in range(10):
    try:
        path_to_image = os.path.join(os.getcwd(), "images", "image_{0}.png".format(i))
        img = get_cleared_from_image(path_to_image)
        img.save(path_to_image.replace("images", "results"))
    except:
        pass
