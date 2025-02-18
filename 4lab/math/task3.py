import math

def area_of_polygon(n, a):

    return (n * a**2) / (4 * math.tan(math.pi / n))
a = int(input())
n = int(input())

area = area_of_polygon(n, a)


print(f"Площадь правильного многоугольника: {area:.2f}")
