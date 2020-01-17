def int_func(text):
    return text.title()

print(int_func(text=input("Введите одно слово: ")))

some_word = int_func(text=input("Введите несколько слов, разделенных пробелами: "))
print(some_word)
