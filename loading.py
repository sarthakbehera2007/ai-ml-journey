import cv2

image= cv2.imread("image1.png")


if image is None:
 print("error:image not found")
else:
 print("image load sucessfully")
