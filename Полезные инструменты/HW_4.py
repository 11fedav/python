my_list = [1, 1, 25, 46, 46, 14, 50, 50, 13]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)