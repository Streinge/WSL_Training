import numpy as np
import sys
import time
t1 = time.perf_counter()

new = np.random.randint(0,255,(5, 5))
print(new)
tuple_needed_index = np.where(new > 200)
point_1, point_2 = np.zeros(2), np.zeros(2)
point_1[1] = tuple_needed_index[0][0]
# координата X первой точки
point_1[0] = tuple_needed_index[1][0]
# аналогично со второй точкой
point_2[0] = tuple_needed_index[1][-1]
point_2[1] = tuple_needed_index[0][-1]
print(point_1, point_2)
dim_not_null = tuple_needed_index[0].shape[0]
not_null = np.zeros([dim_not_null, 2])
for i in range(tuple_needed_index[0].shape[0]):
    not_null[i] = np.array([tuple_needed_index[1][i], tuple_needed_index[0][i]])
print(not_null)
difference = np.zeros(not_null.shape[0])
for i in range(not_null.shape[0]):
    difference[i] = (
        np.abs(
            (point_2[1] - point_1[1]) * not_null[i][0]
            - (point_2[0] - point_1[0]) * not_null[i][1]
            + point_2[0] * point_1[1]
            - point_2[1] * point_1[0]
        )
        / ((point_2[1] - point_1[1]) ** 2 + (point_2[0] - point_1[0]) ** 2) ** 0.5
    )

print(difference)
point_3 = not_null[np.argmax(difference)]

print(point_3)


t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.5f} секунд")