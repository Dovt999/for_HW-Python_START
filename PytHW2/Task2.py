p = int(input('введите произведение этих чисел'))
s = int(input('введите сумму этих чисел'))

for i in range(s):
    for k in range(p):
        if p == i * k and s == i + k:
            print('загаданные числа:', i, k)
