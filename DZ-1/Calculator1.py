a = int(input("Введи число: "))
b = int(input("Введи число: "))
c = str(input("Введи знак: "))

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == '%':
    print(a % b)
elif c == '**':
    print(a ** b)
else:
    print('Ошибка')