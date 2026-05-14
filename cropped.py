import cv2 

image= cv2.imread("image1.png")

if image is not None:
  cropped = image[1000:2000 ,500:1500]


  cv2.imshow("original",image)
  cv2.imshow("cropped",cropped)
  cv2.waitKey(0)
  cv2.destroyAllWindows()