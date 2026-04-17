sumOfdiliveryes = int(input("Введите сумму заказа: "))
regularCustomer = bool(input("Вы регулярный покупатель? (да/нет): "))
wayOfDelivery = int(input("какая доставка?(курьер - 1/самовывоз - 2): "))
promoCode = (input("Введите промокод. "))
sumWithSales = 0

sale = 0

if sumOfdiliveryes > 5000:
    sale += 5
elif sumOfdiliveryes > 10000:
    sale += 10
elif sumOfdiliveryes > 15000:
    sale += 15
if regularCustomer == "yes":
    sale += 5
while True:
    if promoCode == "SUMMER16":
        sale += 10
        break
    elif promoCode == "BIRTHDAY":
        sale += 15
        break
sumWithSales = sumOfdiliveryes * (1 - sale/100)
if wayOfDelivery == 1:
    if(sumOfdiliveryes <= 8000):
        sumWithSales += 500
print(f"итоговая стоимость составляет:  {sumWithSales} рублей.")


