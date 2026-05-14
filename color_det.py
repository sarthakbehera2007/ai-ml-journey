# import cv2
# import numpy  as np

# cap =cv2.VideoCapture(0)

# while True:
#   _,frame =cap.read()


#   hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#   lower_red =np.array([0,120,70])
#   upper_red= np.array([10,255,255])


#   mask = cv2.inRange(hsv,lower_red, upper_red)

#   result = cv2.bitwise_and(frame, frame,mask=mask)

#   cv2.imshow("original",frame)
#   cv2.imshow("MASK",mask)
#   cv2.imshow("DETECTED",result)

#   cv2.waitKey(0)
  



#   cv2.release()
#   cv2.destroyAllWindows()


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

MIN_AREA = 500

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Red
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Green
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])

    # Blue
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    # Yellow
    lower_yellow = np.array([15, 100, 100])
    upper_yellow = np.array([35, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    colors = {
        "RED": (mask_red, (0, 0, 255)),
        "GREEN": (mask_green, (0, 255, 0)),
        "BLUE": (mask_blue, (255, 0, 0)),
        "YELLOW": (mask_yellow, (0, 255, 255))
    }

    y_offset = 30

    for color_name, (mask, color) in colors.items():
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        count = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > MIN_AREA:
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                center = (int(x), int(y))
                radius = int(radius)

                if radius > 10:
                    cv2.circle(frame, center, radius, color, 2)
                    cv2.circle(frame, center, 3, color, -1)

                    cv2.putText(frame, color_name, (center[0] - 20, center[1] - radius - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                    count += 1

        cv2.putText(frame, f"{color_name}: {count}", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        y_offset += 30

    cv2.imshow("Color Detection with Circle", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()