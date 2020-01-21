def my_func(num1, num2):
    if num2 == 0:
       print("На '0' делить нельзя, получится бесконечность")
    else:
        result = num1 / num2
        print(result)

my_func(num1=int(input("Введите 1 число: ")), num2=int(input("Введите 2 число ")))
