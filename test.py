import numpy as np
import sys
import time
t1 = time.perf_counter()
DIM_X = 10
DIM_Y = 10
raw_img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 230, 0], 
                    [0, 0, 215, 0, 0, 0, 0, 240, 0, 0],
                    [0, 0, 0, 0, 195, 0, 196, 0, 0, 0], 
                    [0, 247, 0, 0, 0, 210, 0, 120, 0, 0],
                    [0, 0, 0, 0, 254, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 235, 0, 0, 0, 0, 0, 0],
                    [0, 0, 220, 0, 0, 0, 120, 0, 0, 0], 
                    [0, 245, 0, 0, 0, 0, 0, 0, 0, 0],
                    [210, 0, 0, 0, 0, 0, 0, 130, 0, 0], 
                    [0, 0, 0, 0, 0, 189, 0, 0, 0, 0]])

PI = np.round(np.pi, 8)
THETA_MAX = 180
theta = np.array(np.zeros(THETA_MAX + 1))
for i in range(- int(round(THETA_MAX / 2)), int(round(THETA_MAX / 2)) + 1):
    theta[i] = np.round((PI * i) / 180, 8)
theta = np.sort(theta)

cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
y_test, x_test = np.nonzero(raw_img)
r_max = (DIM_X ** 2 + DIM_Y ** 2) ** 0.5
counter = np.zeros((int(round(2 * r_max)), THETA_MAX), dtype=np.uint8)

for i in range(len(y_test)):
    for theta_0 in range(THETA_MAX):
        r_0 = int(round(x_test[i] * cos_theta[theta_0] + y_test[i] * sin_theta[theta_0]))
        counter[r_0, theta_0] += 1



maxi = counter[np.argmax(counter, axis=0), np.arange(180)]



print(counter)

t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.5f} секунд")