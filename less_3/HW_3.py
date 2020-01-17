def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)


print(my_func(
    num1=int(input("Введите первое число: ")),
    num2=int(input("Введите второе число: ")),
    num3=int(input("Введите третье число: ")),
))