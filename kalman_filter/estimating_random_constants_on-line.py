import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
X = [KF.statePost[0,0]] # 값 배열 초기값
P = [KF.errorCovPost[0,0]] # 사후 오차 추정 공분산 배열 초기값

""" fig 객체 설정 """
fig = plt.figure()
fig.canvas.set_window_title('Kalman Filter')
ax = plt.axes(xlim = (0, N), ylim = (x-3*np.sqrt(r), x+3*np.sqrt(r)))
ax.grid()
line1, = ax.plot([], [], 'b-', lw=2)
line2, = ax.plot([], [], 'rx')
line3, = ax.plot([0,N], [x,x], 'g-') # 참값
xrange = np.arange(N) # x축 범위
Z = [] # 측정값 표시할 배열

""" 애니메이션 초기화 """
def init():
    for k in range(N):
        predict = KF.predict()
        z = np.random.randn(1,1) # 측정값 생성
        estimate = KF.correct(z[0]) # 측정값 정정
        X.append(estimate[0,0])
        Z.append(z[0][0])
    line1.set_data(xrange, X)
    line2.set_data(xrange, Z)

    return line1, line2

""" 애니메이션에 의해 반복 호출되는 함수 """
def animate(k):
    global X, Z

    predict = KF.predict()
    z = np.random.randn(1,1) * np.sqrt(r) + x
    estimate = KF.correct(z[0])

    X = X[1:N]
    X.append(estimate[0,0])

    Z = Z[1:N]
    Z.append(z[0][0])
    line1.set_data(xrange, X)
    line2.set_data(xrange, Z)

    return line1, line2

ani = animation.FuncAnimation(fig, animate, init_func=init, interval=25, blit=True)
plt.show()