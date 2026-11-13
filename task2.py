age_text = input("Возраст!")
ticket = input("Есть билет? (да/нет): ").strip().lower()

if not age_text.isdigit():
    print("ВОзраст должен быть целым числом")
elif ticket != "да" and ticket != "нет":
    print("Ответьте <<да>> или <<нет>> ")
else:
    age = int(age_text)

if age < 16:
    print("Вход запрещен, фильм 16+")

elif ticket == "нет":
    print("Сначла купите билет")
else:
    print("Приятного просмотра")

if age >= 60 or age <18:
    print("У вас скидка на попкорн 20%")