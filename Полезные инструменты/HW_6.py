from itertools import count, cycle

#a
for i in count(int(input('Введите начальное значение: '))):
    print(i)

#b
my_list = [10, 10, 20, 20, 30, 50, 50, 40]

x = cycle(my_list)
stop = ''
while stop != 'e':
    print(next(x), end='')
    stop = input()