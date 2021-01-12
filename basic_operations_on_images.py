import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # 튜플의 행, 열 수와 채널
print(img.size) # 픽셀 크기
print(img.dtype) # 데이터 타입
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390] # 공 위치 픽셀 좌표
img[273:333, 100:160] = ball # 공을 합성할 공간 픽셀 좌표

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, .9, img2, .1, 0);

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()