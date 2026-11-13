
text_sum = input("Сумма заказа: ")
text_people = input("КОличество человек: ") 


if not  text_sum.replace(".", "", 1).isdigit():
    print("Сумма должна быть числом")
elif not text_people.isdigit() or int(text_people) == 0:
    print("КОличестов человек должно быть больше 0")
else:
    order_sum = float(text_sum)
    people = int(text_people) 

    total = round(order_sum * 1.1, 2)
    per_person = round(total / people, 2)

    print("Итого с обслуживанием: total")
    print("С каждого: per_person") 
