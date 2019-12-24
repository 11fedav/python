my_str = input('Введите какое-нибудь предложение: ')
new_str = []
split = my_str.split(' ')
for i, s in enumerate(split, start=1):
    if len(s) <= 10:
        print(i, s)
    else:
        print(i, s[0:10])


