sec = int(input('Введите время в секундах: '))

hour = int(sec / 3600)
hour1 = sec % 3600

minute = int(hour1 / 60)
minute1 = hour1 % 60

second = minute1 % 60

print(hour, ':', minute, ':', second)