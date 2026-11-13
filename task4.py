text = input("Введите n: ")

if not text.isdigit() or int(text) == 0:
    print("n должно  быть целым числом больше 0")
else:
    n = int(text)

    for row in range(1, n + 1)
    if row  % 2 == 0:
        continue 
    for col in range(1, n + 1)
    print(row * col, end="")
    print() 