#Второе задание
seconds = int(input("Введите количество секунд: \n >>>"))
hours = seconds // 3600
minutes = seconds // 60 % 60
seconds = seconds % 60
print(f'Другими словами это "{hours} ч.{minutes} мин.{seconds} сек."')