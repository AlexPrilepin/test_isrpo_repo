import math

def area(r):
  """
  Вычисляет площадь круга по заданному радиусу.
      Параметры:
          r (float): Радиус круга.
      Возвращает:
          float: Площадь круга.
  """

  if(not isinstance(r, (int, float))):
    raise TypeError("R должно быть int или float")
  
  if(r < 0):
    raise ValueError("R не может быть отрицательным"); 

  return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга) по заданному радиусу.
        Параметры:
            r (float): Радиус окружности.
        Возвращает:
            float: Длина окружности.
    """
    
    if(not isinstance(r, (int, float))):
      raise TypeError("R должно быть int или float")
    
    if(r < 0):
      raise ValueError("R не может быть отрицательным"); 
    

    return 2 * math.pi * r

