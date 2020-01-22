my_list = [2, 4, 6, 2, 15, 6, 5, 10]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1]]
print(new_list)
