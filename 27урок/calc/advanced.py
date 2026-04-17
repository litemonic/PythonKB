def power(base, exponent):
    """Вовзведение в степень"""
    return base ** exponent

def sqrt(a):
    """Квадратный корень"""
    if a < 0:
        return "Ошибка отрицательное число"
    else: 
        return a ** 0.5