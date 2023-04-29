n = int (input ('введите количество монеток') )
list_1 = []
print('вводите 0, если монета лежит верх решкой и 1, если гербом')
min = 0
for i in range(n):
    r = input('введите 0 или 1')
    list_1.append(r)
    if r == '0':
        min = min + 1
    print(list_1)

if (n - min) < min:
    min = n - min
print('минимальное число переворачиваемых монеток равно', min)