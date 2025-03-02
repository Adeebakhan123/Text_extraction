import requests
from bs4 import BeautifulSoup
import os

#url='
# Create the "IMAGES" folder if it doesn't existss
if not os.path.exists("Newimg"):













































































    
    os.mkdir("Newimg")

# Ask the user for the image link and file name
image_link = input("Enter the image link: ")
image_name = input("Enter the image file name (with extension): ")

# Download the image
response = requests.get(image_link)
if response.status_code == 200:
    # Save the image inside the "IMAGES" folder
    with open(os.path.join("Newimg", image_name), "wb") as f:
        f.write(response.content)
    print(f"Newimg '{image_name}' has been successfully downloaded and saved in 'newimage' folder.")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")
