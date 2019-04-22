# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle:

    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def tr_square(self):
        s =((self.ax - self.cx) * (self.by - self.cy) - (self.ay - self.cy) * (self.bx - self.cx)) / 2
        return s

    def tr_perimeter(self):
        ab = math.sqrt(((self.bx - self.ax) ** 2) + ((self.by - self.ay) ** 2))
        ac = math.sqrt(((self.cx - self.ax) ** 2) + ((self.cy - self.ay) ** 2))
        bc = math.sqrt(((self.cx - self.bx) ** 2) + ((self.cy - self.by) ** 2))
        return ab + ac + bc
    def tr_height(self):
        v = ((self.by - self.cy) * self.ax) + ((self.cx - self.bx) * self.ay) + ((self.bx * self.cy) - (self.cx * self.by)) / math.sqrt(((self.by - self.cy) ** 2) + ((self.cx - self.bx) **2))
        return v


tr1 = Triangle(3,2,7,5,0,0)

print(tr1.tr_square())
print(tr1.tr_perimeter())
print(tr1.tr_height())
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.