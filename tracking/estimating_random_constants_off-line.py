import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

x = -0.37727 # 참값
q = 1e-5 # 프로세스 잡음 공분산 분포
r = 0.01 # 측정 잡음 공분산 분포

""" 칼만 필터 객체 KF 생성 """
KF = cv.KalmanFilter(1,1,0) # 외부 입력 행렬 0
KF.transitionMatrix = np.ones((1,1)) # 상태 변환 행렬 1
KF.measurementMatrix = np.ones((1,1)) # 측정 행렬 1
KF.processNoiseCov = q * np.eye(1) # 프로세스 잡음 공분산
KF.measurementNoiseCov = r * np.eye(1) # 측정 잡음 공분산

""" 초기화 및 초기값 설정 """
KF.errorCovPost = np.ones((1,1))
KF.statePost = np.zeros((1,1))

N = 50
z = np.random.randn(N,1) * np.sqrt(r) + x # 측정값
X = [KF.statePost[0,0]] # 값 배열 초기값
P = [KF.errorCovPost[0,0]] # 사후 오차 추정 공분산 배열 초기값

""" 예측 및 측정 """
for k in range(1, N):
    predict = KF.predict() # 예측 상태
    estimate = KF.correct(z[k]) # 정정 상태
    X.append(estimate[0,0])
    P.append(KF.errorCovPost[0,0])

""" 도식화 """
plt.figure(1)
plt.xlabel('k'), plt.ylabel('X(k)')
plt.axis([0, N, x-3*np.sqrt(r), x+3*np.sqrt(r)])
plt.plot([0,N], [x,x], 'g-')
plt.plot(X, 'b-')
plt.plot(z, 'rx')

plt.figure(2)
plt.xlabel('k'), plt.ylabel('P(k)')
plt.axis([0, N, 0, 1.0])
plt.plot(P, 'b-')

plt.show()