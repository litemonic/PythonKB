def calculate_imt(weight_kg: float, heigth_m: float) -> float:
    """
    Рассчет индекса массы тела
    Формула: вес(кг) / рост(м)^2 
    """
    if weight_kg <= 0:
        raise ValueError('Вес не может быть отрицательным. Вы антиматерия?')
    if heigth_m <= 0:
        raise ValueError('Рост должен быть больше 0')
    return weight_kg / heigth_m ** 2

def get_imt_category(imt:float) -> str:
    if imt < 16:
        return "Выраженный дефицит массы"
    elif imt < 18.5:
        return "Недостаточная масса тела"
    elif imt < 25:
        return "Норма"
    elif imt < 30:
        return "Избыточная масса тела"
    elif imt < 35:
        return "Ожирение I степени"
    elif imt < 40:
        return "Ожирение II степени"
    else:
        return "Ожирение III степени"


def isTrue(bmi: float) -> bool:
    """
    возвращает True, если ИМТ >= 25
    """
    return bmi >= 25
