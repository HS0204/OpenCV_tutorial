import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img/lena.jpg', -1)
cv.imshow('image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([]) # 그래프에서 x축 y축 숨기기
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()