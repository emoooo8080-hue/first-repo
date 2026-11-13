secret = 37
max_attempts = 5 
attemptss = 1
guessed = False 

while attemptss <= max_attempts:
    text = input(f"Попытка, {attemptss}:")

    if not text.isdigit():
        print("Введите целое число")
        continue
    guess = int(text)

    if guess == secret:
        print(f"Угадал c {attemptss}-й попытки!")
        guessed = True 
        break 
    elif guess > secret:
        print("Меньше")
    else:
        print("Больше")

    attemptss =+1

    if not guessed:
        print("Попытки закончились. Загаданное число: secret")
