import numpy as np
import sys
import time
t1 = time.perf_counter()
DIM_X = 10
DIM_Y = 10
raw_img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 250, 0, 0, 0, 0, 0],
                    [0, 0, 0, 250, 0, 250, 0, 0, 0, 0], 
                    [0, 0, 250, 0, 0, 0, 250, 0, 0, 0],
                    [0, 250, 0, 0, 0, 0, 0, 250, 0, 0], 
                    [250, 250, 250, 250, 250, 250, 250, 250, 250, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

PI = np.round(np.pi, 8)
print(PI)
theta = np.array([[- np.round(4 * PI / 8, 8)],
                  [- np.round(3 * PI / 8, 8)],
                  [- np.round(2 * PI / 8, 8)],
                  [- np.round(1 * PI / 8, 8)],
                  [0],
                  [np.round(1 * PI / 8, 8)],
                  [np.round(2 * PI / 8, 8)],
                  [np.round(3 * PI / 8, 8)],
                  [np.round(4 * PI / 8, 8)]])

cos_theta = np.cos(theta)
sin_theta = np.sin(theta)

y_test, x_test = np.nonzero(raw_img)

r_max = (DIM_X ** 2 + DIM_Y ** 2) ** 0.5
counter = np.zeros((int(round(2 * r_max)), 9), dtype=np.uint8)

for i in range(len(y_test)):
    for theta_0 in range(9):
        r_0 = int(np.round(x_test[i] * cos_theta[theta_0] + y_test[i] * sin_theta[theta_0]))
        counter[r_0, theta_0] += 1
print(counter)
print(np.shape(counter))
print(np.amax(counter))
count_max = np.sort(counter.flatten())[-3:]
print(count_max)
line_1 = count_max[0]
line_2 = count_max[1]
line_3 = count_max[2]
param_line_1 = np.where(counter == line_1)
param_line_2 = np.where(counter == line_2)
param_line_3 = np.where(counter == line_3)
print(x_test)
for x in x_test:
    y1 = (x * cos_theta[param_line_1[1]][0][0] - param_line_1[0][0]) / sin_theta[param_line_1[1]][0][0]
    y2 = (x * cos_theta[param_line_2[1]][0][0] - param_line_2[0][0]) / sin_theta[param_line_2[1]][0][0]
    print('x ', x, ' y2-y1 ', abs(y2 - y1))

print(param_line_1[0], theta[param_line_1[1]])



t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.5f} секунд")
