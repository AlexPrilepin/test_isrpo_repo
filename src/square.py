
def area(a):
    """
    Вычисляет площадь квадрата по заданной длине стороны.
        Параметры:
            a (float): Длина стороны квадрата
        Возвращает:
            float: Площадь квадрата.
    """

    if not isinstance(a, (int, float)):
      raise TypeError("Ожидается int или float")
    
    if a < 0:
      raise ValueError("Число не может быть отрицательным")

    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата по заданной длине стороны.
        Параметры:
            a (float): Длина стороны квадрата.
        Возвращает:
            float: Периметр квадрата.
    """

    if not isinstance(a, (int, float)):
      raise TypeError("Ожидается int или float")
    
    if a < 0:
      raise ValueError("Число не может быть отрицательным")
    
    return 4 * a
