my_list = []

for i in range(5):
    my_list.append(int(input('Введите 5 чисел: ')))

j = 0

for i in range(int(len(my_list) / 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2

print(my_list)
