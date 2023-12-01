import numpy as np
import sys
import time

img_path = '/home/streinge/WSL_Training/0.0/00.pgm'
# img_path = '/home/streinge/0.1/00.pgm'
t1 = time.perf_counter()
DIM_X = 500
DIM_Y = 500
# np.loadtxt записывает в ОДНОМЕРНЫЙ массив изображение из файла, 
# исключая первые три строки, разделитель пробел, тип целые числа от нуля до 255
# np.reshape преобразует полученный одномерный массив в массив с размером 500х500
raw_img = np.loadtxt(img_path, skiprows=3, delimiter=' ',dtype=np.uint8).reshape((DIM_X, DIM_Y))
# считаем процент черных точек на изображении
count_black = raw_img[raw_img == 0].shape[0] / (DIM_X *DIM_Y)
print('процент черных точек ', count_black)
""" if count_black > 0.9:    
    # задаем координаты двух точех с помощью np.zeros(2) (создание одномерного массива нулей)
    point_1, point_2 = np.zeros(2), np.zeros(2)
    # np.where формирует кортеж из двух элементов, каждый из которых np.array, которые содержат
    # индексы удовлетворяющих условиям элементов из raw_img, при этом получается, что номер 
    # строки = это координата Y точки, а номер столбца координата X точки. Поэтому присваивание
    # в координатах идет наоборот
    tuple_needed_index = np.where(raw_img != 0)
    # координата Y первой точки
    point_1[1] = tuple_needed_index[0][0]
    y1 = point_1[1]
    # координата X первой точки
    point_1[0] = tuple_needed_index[1][0]
    x1 = point_1[0]
    # аналогично со второй точкой
    point_2[0] = tuple_needed_index[1][-1]
    x2 = point_2[0]
    point_2[1] = tuple_needed_index[0][-1]
    y2 = point_2[1]
    # атрибут .shape возвращает размерность массива в виде кортежа (ndim,), поэтому ниже берется 
    # .shape[0] элемент для определение размерности массива и потом создается нулевая матрица not_null
    # размерностью 2 на количество точек удовлетворяющих условию
    # размерность при этом равна
    print(point_1, point_2 )
    dim_not_null = tuple_needed_index[0].shape[0]
    not_null = np.zeros([dim_not_null, 2])
    # заполняем массив ненулевых точек изображения
    for i in range(tuple_needed_index[0].shape[0]):
        not_null[i] = np.array([tuple_needed_index[1][i], tuple_needed_index[0][i]])
    # cчитаем площади всех возможных треугольников
    area_triangle = np.zeros(not_null.shape[0])
    for i in range(not_null.shape[0]):
        area_triangle[i] = abs(0.5 *((x1 - not_null[i][0]) * (y2 - not_null[i][1]) - (x2 - not_null[i][0]) * (y1 - not_null[i][1])))
    # определяем координату третьей точки по максимальной площади треугольника
    point_3 = not_null[np.argmax(area_triangle)]
    print(point_3) """

print('Будем делать преобразование Хафа')
PI = np.round(np.pi, 8)
THETA_MAX = 180
theta = np.array(np.zeros(THETA_MAX + 1))

t_part1 = time.perf_counter()


for i in range(0, THETA_MAX  + 1):
    theta[i] = np.round((PI * i) / THETA_MAX, 8)
theta = np.sort(theta)

cos_theta = np.cos(theta)
sin_theta = np.sin(theta)


# значения координат ненулевых значений яркости изображения
# np.nonzero возвращает кортеж двух массивов в первом индекс строки 
# ненулевого элемента, а во втором - столбца ненулевого элемента
y_test, x_test = np.nonzero(raw_img)
print(np.shape(np.nonzero(raw_img)))
r_max = (DIM_X ** 2 + DIM_Y ** 2) ** 0.5
# создаю массив счетчка с размерностью максимально возомжного размера 
counter = np.zeros((int(round(r_max * 2)), THETA_MAX), dtype=np.uint8)
print(np.shape(counter))
print(len(x_test))

for i in range(len(x_test)):
    for theta_0 in range(THETA_MAX):
        r_0 = int(round(r_max)) + int(np.round(x_test[i] * cos_theta[theta_0] + y_test[i] * sin_theta[theta_0]))
        counter[r_0, theta_0] += 1

# maxi = counter[np.argmax(counter, axis=0), np.arange(180)]
# схлопываем многомерный numpy массив в одномерный массив и сразу в обычный список
count_flatten = counter.flatten()
print(np.shape(count_flatten))
local_maxima = np.where((count_flatten[1:-1] > count_flatten[:-2]) & (count_flatten[1:-1] > count_flatten[2:]))[0] + 1
print(np.shape(local_maxima))

count_max = np.sort(counter.flatten())[-3:]
print(count_max)
line_1 = count_max[0]
line_2 = count_max[1]
line_3 = count_max[2]
param_line_1 = np.where(counter == line_1)
param_line_2 = np.where(counter == line_2)
param_line_3 = np.where(counter == line_3)
print(param_line_1[0] - r_max, theta[param_line_1[1]] * 180 / PI)  
print(param_line_2[0] - r_max, theta[param_line_2[1]] * 180 / PI)  
print(param_line_3[0] - r_max, theta[param_line_3[1]] * 180 / PI)

a = - (np.cos(param_line_1[1]) / np.sin(param_line_1[1]))
c = (param_line_1[0]) / np.sin(param_line_1[1])
b = - (np.cos(param_line_2[1]) / np.sin(param_line_2[1]))
d = (param_line_2[0]) / np.sin(param_line_2[1])
x = (d - c) / (a - b)
y = (a * d - b * c) / (a - b)
print(x, y)





# Это я нашел параметры индексы прямой с наибольшим значением счетчика
# Дальше была идея вывести все точки из изображения, которые принадлежат этой прямой с какой то дельтой
# и сравить с координатами, которые есть в решении, чтобы понять вообще я правильно думаю
    



t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")
