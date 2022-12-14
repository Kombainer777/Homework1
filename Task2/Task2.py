# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату X:  '))
y = int(input('Введите координату Y:  '))
if x == 0 and y == 0:
    print('Ошибка, в данной программе X и Y не могут быть равны 0 одновременно')
elif x > 0 and y > 0:
    print('Точка находится в 1-ой четверти координат')
elif x < 0 and y < 0:
    print('Точка находится в 3-ей четверти координат')
elif x > 0 and y < 0:
    print('Точка находится в 4-ой четверти координат')
elif x < 0 and y > 0:
    print('Точка находится в 2-ой четверти координат')
elif x == 0 and y != 0:
    print('Точка находится на оси Y')
elif x != 0 and y == 0:
    print('Точка находится на оси X')