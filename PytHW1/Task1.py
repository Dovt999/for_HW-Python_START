print('Введите число')
a = int(input())
sum = 0
i = -1 

while i <= len(str(a)):
    sum = sum + a%10
    a //= 10
    i+=1
print(sum)
