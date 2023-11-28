import numpy as np
import sys
import time

img_path = '/home/streinge/WSL_Training/0.1/01.pgm'
t1 = time.perf_counter()
# np.loadtxt записывает в ОДНОМЕРНЫЙ массив изображение из файла, 
# исключая первые три строки, разделитель пробел, тип целые числа от нуля до 255
# np.reshape преобразует полученный одномерный массив в массив с размером 500х500
raw_img = np.loadtxt(img_path, skiprows=3, delimiter=' ',dtype=np.uint8).reshape((500, 500))
# считаем процент черных точек на изображении
count_black = raw_img[raw_img == 0].shape[0] / 250000
print('процент черных точек ', count_black)
if count_black > 0.9:    
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
    for i in range(tuple_needed_index[0].shape[0]):
        not_null[i] = np.array([tuple_needed_index[1][i], tuple_needed_index[0][i]])
    area_triangle = np.zeros(not_null.shape[0])
    for i in range(not_null.shape[0]):
        area_triangle[i] = abs(0.5 *((x1 - not_null[i][0]) * (y2 - not_null[i][1]) - (x2 - not_null[i][0]) * (y1 - not_null[i][1])))
    point_3 = not_null[np.argmax(area_triangle)]
    print(point_3)
else:
    print('Будем делать преобразование Хафа')
    print('число ПИ ', np.round(np.pi, 8))
    theta = np.array(180)
    print(theta)








t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")