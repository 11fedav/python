def information(**kwargs):
    return kwargs

print(information(
    name=input("Введите имя: "),
    second_name=input("Введите фамилию: "),
    bitrhday=input('День рождения: '),
    city=input('Город: '),
    email=input('Почта: '),
    phone=input('Телефон: '),
))