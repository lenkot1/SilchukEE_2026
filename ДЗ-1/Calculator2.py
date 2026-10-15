a = int(input("Введи число: "))
b = int(input("Введи число: "))
c = str(input("Введи знак: "))
def plus(a,b):
    print(a+b)
def minus(a,b):
    print(a-b)
def umnoj(a,b):
    print(a*b)
def delit(a,b):
    print(a/b)
if c == '+':
    plus(a,b)
elif c == '-':
    minus(a,b)
elif c == '*':
    umnoj(a,b)
elif c == '/':
    delit(a,b)
else:
    print('Ошибка')