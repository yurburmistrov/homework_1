number = int(input("Введите целое положительное число : \n"))
figure = number % 10
number_new = number // 10

if number_new <= 0:
    print('Число не является положительным!')
else:
    while number_new > 0:
        if number_new % 10 > figure:
            figure = number_new % 10
        number_new = number_new // 10

    print(f'\nНаибольщая цифра в числе {number} - это {figure}')
