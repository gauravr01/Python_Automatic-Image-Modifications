import cv2
import numpy as np

# Load the image
image_path = 'dhoni.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary mask
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours in the binary mask
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask with white background
mask = np.ones_like(image) * 255

# Draw the detected contours on the mask (fill the contours with black)
cv2.drawContours(mask, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

# Invert the mask to keep the main subject
mask_inverse = cv2.bitwise_not(mask)

# Apply the mask to the original image
result = cv2.bitwise_and(image, mask_inverse)

# Load the new background image
new_bg = cv2.imread('bg.jpg')
print("Original new_bg shape:", new_bg.shape)

# Resize the new background image to match the dimensions of the result image
new_bg = cv2.resize(new_bg, (result.shape[1], result.shape[0]))

# Combine the main subject and the new background
final_result = cv2.bitwise_or(result, new_bg)

# Display the final result
cv2.imshow('Final Result', final_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
