n = int(input('введите число n'))
m = int(input('введите число m'))
list_1 = []
list_2 = []
print('начинаем ввод списка 1')
for i in range(n):
    r = int(input('введите число'))
    list_1.append(r)

print('начинаем ввод списка 2')
for i in range(m):
    r = int(input('введите число'))
    list_2.append(r)

list_result = list_1 + list_2
list_result = set(list_result)
print(list_result)
