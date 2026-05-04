import math

def square(side):
    """Функция вычисляет площадь квадрата"""
    return math.ceil(side * side)

# Пример вызова
side = 5.2
print(f"Площадь квадрата со стороной {side}: {square(side)}")