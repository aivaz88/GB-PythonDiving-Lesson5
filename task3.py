# Создайте функцию генератор чисел Фибоначчи

def fibonachi(num: int = 10) -> int:
    first, second = 0, 1
    while num > 0:
        yield first
        first, second = second, first + second
        num -= 1

for i in fibonachi():
    print(i)