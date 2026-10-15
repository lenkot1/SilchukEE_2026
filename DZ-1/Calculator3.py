def abc(a1, b1, c1):
    if c1 == '+':
        print(a1 + b1)
    elif c1 == '-':
        print(a1 - b1)
    elif c1 == '*':
        print(a1 * b1)
    elif c1 == '/' and b1 != 0:
        print(a1 / b1)
    elif c1 == '//' and b1 != 0:
        print(a1 // b1)
    elif c1 == '%' and b1 != 0:
        print(a1 % b1)
    elif c1 == '**':
        print(a1 ** b1)
    else:
        print('Ошибка')
while True:
    a = int(input("Введи число: "))
    b = int(input("Введи число: "))
    c = str(input("Введи знак: "))
    abc(a, b, c)