# import cv2

# image= cv2.imread("image1.png")

# if image is None:
#   print("not found")
# else:
#   {h,w} = image.shape[:2]

#   center=(w//2,h//2)
#   M= cv2.getRotationMatrix2D(center,90,1.0)
#   rotated=cv2.warpAffine(image,M,(w,h))


#   cv2.imshow("original",image)
#   cv2.imshow("rotated 90 degree",rotated)

#   cv2.waitKey(0)
#   cv2.destroyAllWindows()