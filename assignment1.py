import cv2

image= cv2.imread("image1.png")

if image is not None:

 cv2.imshow("image1.png",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


  




