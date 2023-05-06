n = int(input('введите количество кустов'))
list_1 = []
list_2 = []
for i in range(n):
    r = int(input('введите кол-во ягод на кусте'))
    list_1.append(r)
    print(r)
i = 0

while i < len(list_1):
    if i == 0:
        sum3 = list_1[n - 1] + list_1[i] + list_1[i + 1]
    if i == len(list_1)-1:
        sum3 = list_1[i - 1] + list_1[i] + list_1[0]
    else:
        sum3 = list_1[i - 1] + list_1[i] + list_1[i + 1]
    list_2.append(sum3)
    print(sum3)
    i += 1
print(max(list_2))
