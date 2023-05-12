def step(A, B):
    if B == 1:
        return 1
    else:
        return A*step(A, B-1)

A = int(input('введите A'))
B = int(input('введите B'))
print(step(A, B))

