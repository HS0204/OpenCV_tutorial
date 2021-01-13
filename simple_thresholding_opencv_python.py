import cv2
import numpy as np

img = cv2.imread('./img/gradient.png', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) # 50보다 작으면(블랙에 가까우면) 0(black), 50~255면 1
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV) # 200보다 작으면 1, 200~255면 0
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # threshold(127)보다 작은 구간 0(black)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # threshold보다 큰 구간 0(black)

cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()