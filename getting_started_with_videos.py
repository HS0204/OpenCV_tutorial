import cv2

cap = cv2.VideoCapture(0); # 0을 사용하면 디폴트 카메라(웹캠)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 비디오 코덱
out = cv2.VideoWriter('./img/output.avi', fourcc, 20.0, (640,480)) # output이란 이름의 640x480 비디오를 fourcc에 저장된 코덱으로 20초 동안 녹화

print(cap.isOpened())

while(cap.isOpened()): # cap이 제대로 열렸을 때만 True 반환. 아닐 시 False
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 프레임 길이 구함
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 프레임 높이 구함

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # BGR을 GRAY로 변경
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 반복문 탈출
            break
    else:
        break

cap.release() # cap을 화면에 띄움
out.release() # 녹화되고 있는 out을 같은 폴더에 저장함
cv2.destroyAllWindows()