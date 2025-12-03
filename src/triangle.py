def area(a, h): 
    """
    Вычисляет площадь треугольника по основанию и высоте.
        Параметры:
            a (float): Длина основания треугольника.
            h (float): Высота треугольника, проведенная к основанию.
        Возвращает:
            float: Площадь треугольника.
    """

    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
      raise TypeError("Ожидается int или float")
    
    if a < 0 or h < 0:
      raise ValueError("Число не может быть отрицательным")
    
    return a * h / 2 

def perimeter(a, b, c): 
    """
    Вычисляет периметр треугольника по длинам трех сторон.
        Параметры:
            a (float): Длина первой стороны треугольника.
            b (float): Длина второй стороны треугольника.
            c (float): Длина третьей стороны треугольника.
        Возвращает:
            float: Периметр треугольника.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
      raise TypeError("Ожидается int или float")
    
    if a < 0 or b < 0 or c < 0:
      raise ValueError("Число не может быть отрицательным")
    
    return a + b + c 
