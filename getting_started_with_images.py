import cv2

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27: # esc 키를 누른다면 종료
    cv2.destroyAllWindows()
elif k == ord('s'): # s키를 누른다면 저장 후 종료
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()