import cv2
import os
def remove_horizontal_and_vertical_lines(image):
  # Convert the image to grayscale.
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding to the image to obtain a binary image.
  thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  # Create a structuring element for morphological operations.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

  # Apply morphology operations to the image to remove horizontal and vertical lines.
  eroded_image = cv2.erode(thresh_image, kernel, iterations=2)
  dilated_image = cv2.dilate(eroded_image, kernel, iterations=2)

  # Invert the image to obtain the final result.
  final_image = cv2.bitwise_not(dilated_image)

  return final_image
# Load the image
image = cv2.imread("")
input_image = cv2.imread(image)
output_image = remove_horizontal_and_vertical_lines(input_image)

# Save the output image.
output_image_path = "output.jpg"
cv2.imwrite(output_image_path, output_image)

# Print a message to the console.
print("The output image has been saved to {}".format(output_image_path))


