N = input('введите N').upper()
list_1 = []
value = 0
for i in range(len(N)):
    if N[i] == 'A' or N[i] == 'E' or N[i] == 'I' or N[i] == 'O' or N[i] == 'U 'or N[i] == 'L' or N[i] == 'N' or N[i] == 'S' or N[i] == 'T' or N[i] == N[i] == 'A' or N[i] == 'E' or N[i] == 'I' or N[i] == 'O' or N[i] == 'U' or N[i] == 'L' or N[i] == 'N' or N[i] == 'S' or N[i] == 'T' or N[i] == 'R':
        value = value + 1
    if N[i] == 'D' or N[i] == 'G':
        value = value + 2
    if N[i] == 'B' or N[i] == 'C' or N[i] == 'M' or N[i] == 'P':
        value = value + 3
    if N[i] == 'F' or N[i] == 'H' or N[i] == 'V' or N[i] == 'W' or N[i] == 'Y':
        value = value + 4
    if N[i] == 'K':
        value = value + 5
    if N[i] == 'J' or N[i] == 'X':
        value = value + 8
    if N[i] == 'Q' or N[i] == 'Z':
        value = value + 10
    if N[i] == 'А' or N[i] == 'В' or N[i] == 'Е' or N[i] == 'И' or N[i] == 'Н' or N[i] == 'О' or N[i] == 'Р' or N[i] == 'С' or N[i] == 'Т':
        value = value + 1
    if N[i] == 'Д' or N[i] == 'К' or N[i] == 'Л' or N[i] == 'М' or N[i] == 'П' or N[i] == 'У':
        value = value + 2
    if N[i] == 'Б' or N[i] == 'Г' or N[i] == 'Ё' or N[i] == 'Ь' or N[i] == 'Я':
        value = value + 3
    if N[i] == 'Й' or N[i] == 'Ы':
        value = value + 4
    if N[i] == 'Ж' or N[i] == 'З' or N[i] == 'Х' or N[i] == 'Ц' or N[i] == 'Ч':
        value = value + 5
    if N[i] == 'Ш' or N[i] == 'Э' or N[i] == 'Ю':
        value = value + 8
    if N[i] == 'Ф' or N[i] == 'Щ' or N[i] == 'Ъ':
        value = value + 10

print(value)






