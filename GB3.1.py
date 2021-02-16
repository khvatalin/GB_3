def delenie(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return 'Низя делить на 0! Кусь'
print(delenie(int(input()), int(input())))
