N = int(input('введите N'))
X = int(input('введите X'))
list_1 = []
close = 0 
print('Вводите цифры по команде')
for i in range(N):
    r = int(input('Введите число'))
    list_1.append(r)
    if abs(X - r) < abs(X - close):
        close = r
print(close)


