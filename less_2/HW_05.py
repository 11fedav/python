my_list = [7, 5, 3, 3, 2]

new_number = int(input('Введите любое натуральное число: '))

for i in range(len(my_list)):
    if new_number > my_list[i]:
        my_list.insert(i, new_number)
        break
    elif new_number <= my_list[-1]:
        my_list.append(new_number)
        break

print(my_list)

