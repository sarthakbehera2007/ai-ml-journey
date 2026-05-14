import cv2

image= cv2.imread("image1.png")

if  image is   None:
  print("image not found")
else :
  print("image loaded")

  resized=cv2.resize(image,(300,300))

  cv2.imshow("Original image",image)
  cv2.imshow("resized image",resized)

  cv2.imwrite("resized_output.png",resized)