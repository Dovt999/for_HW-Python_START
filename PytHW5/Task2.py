def step(A, B):
    if B == 0:
        return A
    else:
        return step(A + 1, B - 1)

A = int(input('введите A'))
B = int(input('введите B'))
print(step(A, B))
