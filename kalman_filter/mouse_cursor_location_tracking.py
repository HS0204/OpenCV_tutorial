import cv2 as cv
import numpy as np

""" 마우스 이벤트 핸들러 """
def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK: # 더블 클릭 시 초기화
        param[0][:,:] = 0 # 영상 프레임 전달 받음
    # 마우스 좌표 저장
    param[1][0] = x
    param[1][1] = y

""" 컬러 영상 생성 """
frame = np.zeros((512,512,3), np.uint8)
z = np.zeros((2,1), np.float32) # 마우스 위치 측정값

cv.namedWindow('Kalman Filter')
cv.setMouseCallback('Kalman Filter', onMouse, [frame, z])

""" 칼만 필터 객체 생성 """
q = 1e-5 # 프로세스 잡음 공분산 분포
r = 0.01 # 측정 잡음 공분산 분포
KF = cv.KalmanFilter(4,2,0) # 상태 벡터 차원 4, 측정 벡터 차원 2, 외부 컨트롤 사용X
KF.transitionMatrix = np.array([[1,0,1,0],
                                [0,1,0,1],
                                [0,0,1,0],
                                [0,0,0,1]], np.float32) # 상태 변환 행렬
KF.measurementMatrix = np.array([[1,0,0,0],
                                 [0,1,0,0]], np.float32) # 측정 행렬
KF.processNoiseCov = q * np.eye(4, dtype=np.float32) # 프로세스 잡음 공분산
KF.measurementNoiseCov = r * np.eye(2, dtype=np.float32) # 측정 잡음 공분산

""" 초기값 """
KF.errorCovPost = np.eye(4, dtype=np.float32)
KF.statePost = np.zeros((4,1), dtype=np.float32)

# 이전 측정값, 초기값 복사
last_z = z.copy()
last_estimate = KF.statePost.copy()

""" 예측 및 측정 """
while True:
    predict = KF.predict()
    estimate = KF.correct(z)

    x1, y1 = np.int0(last_z)
    x2, y2 = np.int0(z)
    cv.line(frame, (x1[0], y1[0]), (x2[0], y2[0]), (0, 0, 255), 2)

    x1, y1, _, _ = np.int0(last_estimate)
    x2, y2, _, _ = np.int0(estimate)
    cv.line(frame, (x1[0], y1[0]), (x2[0], y2[0]), (255, 0, 0), 2)
    cv.imshow('Kalman Fliter', frame)

    last_z = z.copy()
    last_estimate = estimate.copy()

    key = cv.waitKey(30)
    if key == 27: break
cv.destroyAllWindows()
