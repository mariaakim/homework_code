# Урок 1
imya=input("Введите имя:\n")
print("Привет,",imya,", давайте познакомимся!") 

# Урок 2
name=("Мария")
print("Меня зовут",name)
age=(22)
print("Мне",age)
height=("167 см")
print("Мой рост",height)
weight=("60 кг")
print("Мой вес",weight)
bmi=("21,5")
print("Мой ИМТ", bmi)

# Урок 3
score = int(input("Введите количество очков:\n"))
if score > 89:
    print("Отлично!")
elif score > 69 and score < 90:
    print("Хорошо!")
elif score < 70:
    print("Попробуйте ещё раз!")

# Урок 4
import random
number=int(input("С какой попытки ты сможешь угадать число от 1 до 10, которое я загадала? Впиши количество попыток:\n"))
a = random.randint(1,10)
for i in range(1, number+1):
    x = int(input(f"Попытка {i}:\n"))
    if x == a:
        print("Ты победил! Я загадала",a)
        break
    else:
        print("Не угадал(")
        if i == number:
            print(f"Ты проиграл, я загадала число",a)
            break