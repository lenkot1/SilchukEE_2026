class Сalculator():

    def abc(self, a1, b1, c1):
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
        elif c1 == '**':
            print(a1 ** b1)
        elif c1 == '%' and b1 != 0:
            print(a1 % b1)
        else:
            print('ОШИБКА')

calc = Сalculator()

while True:
    a = int(input('ВВЕДИ 1 ЧИСЛО: '))
    b = int(input('ВВЕДИ 2 ЧИСЛО: '))
    c = str(input('ВВЕДИ ЗНАК: '))
    calc.abc(a, b, c)
