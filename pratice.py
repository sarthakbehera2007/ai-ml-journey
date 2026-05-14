# import cv2

# image= cv2.imread("image5.png")

# if image is None:
#  print("error")
# else:
#  cv2.imshow("hello",image)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
#  import cv2
# image =cv2.imread("image1.png")

# if image is not None:
#  cv2.imshow("hi",image)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
# else:
#  print("error") 


# import cv2 

# image=cv2.imread("image5.png")

# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# if image is not None :
#   cv2.imshow("hello",image)
#   cv2.imshow("hi",gray)
#   cv2.waitKey(0)
#   cv2.destroyAllWindows()

# else:
#   print("error")


# import cv2

# image = cv2.imread("image5.png")

# if image is  not None:
#   h,w,c= image.shape
#   print(
#     f"imageloaded \n height:{h} \n width:{w} colomn:{c}"
#   )

# else :
#   print("error")



# import cv2

# image= cv2.imread("image1.png")

# if image is None:
#   print("not loaded")
# else :
#   flipped_horizontal =cv2.flip(image,1)
#   flipped_vertical=cv2.flip(image,0)
#   flipped_both=cv2.flip(image,-1)


#   cv2.imshow("Original",image)
#   cv2.imshow("flipped_horizontal",flipped_horizontal)
#   cv2.imshow("flipped_vertical",flipped_vertical)
#   cv2.imshow("flipped_both",flipped_both)


# cv2.waitKey(0)
# cv2.destroyAllWindows() 


import cv2
 

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
  cv2.waitKey(0)
  cv2.destroyAllWindows()