from functools import reduce

def my_f(num1, num2):
    return num1 * num2

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_f, my_list))
