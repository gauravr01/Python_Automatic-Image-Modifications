import cv2
import os

img = cv2.imread('dhonii.png') #Path of an image
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
faces = faceCascade.detectMultiScale(img,1.1,4)
# Specify the location where you want to create the output directory
output_parent_directory = 'D:\Adobe'

output_directory = os.path.join(output_parent_directory, 'face_images_folder')

try:
    os.mkdir(output_directory)
except FileExistsError as fee:
    print('Output directory already exists:', fee)

# Change working directory to the output directory
try:
    os.chdir(output_directory)
    print('Working directory changed to:', output_directory)
except Exception as e:
    print('Error changing working directory:', e)

def eface():
    i = 1
    for (x, y, w, h) in faces:
        print("Detected face coordinates:", x, y, w, h)
        FaceImg = img[y:y+h, x:x+w]
        # To save an image on disk
        filename = 'Facess' + str(i) + '.jpg'
        print("Saving face image as:", filename)
        cv2.imwrite(filename, FaceImg)
        i += 1

eface()


# Print the shape of the image
print("Image shape:", img.shape)

# Print the detected faces
print("Detected faces:", faces)

# Rest of your code...
