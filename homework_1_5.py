revenue = float(input ("Введите выручку фирмы: \n >>>" ))
costs = float(input ("Введите издержки : \n >>>"))
profit = revenue - costs

if profit > 0:
    print ("Поздравляем, Ваша фирма работает с прибылью")
    rent = profit/revenue
    print("Рентабельность равна", rent)
    person = int(input ("Введите количество работников на вашем предприятии \n"))
    print("Прибыль компании из расчета на каждого сотрудника составляет \n", profit/person )
else:
    print("К сожалению, Ваша фирма в убытке...")