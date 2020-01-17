def my_func(x, y):
    res = x
    for i in range(abs(y) - 1):
        res *= x
    return 1 / res

print(my_func(
    x=float(input("Введите значение x: ")),
    y=int(input("Введите значение y: ")),
))