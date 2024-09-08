import math as m
side = input('введите число')
number = float(side)
def square():
    area = number **2
    if isinstance(number, int) or isinstance(number, float):
        return area
    else:
        return m.ceil(area)

print('площадь квадрата =', square())

