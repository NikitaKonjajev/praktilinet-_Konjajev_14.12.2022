﻿from random import *
from math import *


#4Определить по дню и месяцу рождения пользователя кто он по гороскопу. Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!

print("Определить по дню и месяцу рождения кто ты по гороскопу")
a=int(input("Каой у тебя день рождения?: "))
b=int(input("Какой у тебя месяц рождения?: "))

input("1==а")
input("2==а")
input("3==а")
input("4==Рааак")
input("5==Леав")
input("6==август")
input("7==Веасы")
input("8==Скорапион")
input("9==Стараелец")
input("10==Коаазерог")
input("11==Ваоаы")

if (a>=21 and a<=31 and b==3) or (b==4 and a>=1 and a<=19):
   print("Карты говорят, что ты: Овен")

elif (a>=20 and a<=30 and b==4) or (b==5 and a>=1 and a<=20):
   print("Карты говорят, что ты: Телец")

elif (a>=21 and a<=31 and b==5) or (b==6 and a>=1 and a<=20):
   print("Карты говорят, что ты: Близнецы")

elif (a>=21 and a<=30 and b==6) or (b==7 and a>=1 and a<=22):
   print("Карты говорят, что ты: Рак")

elif (a>=23 and a<=31 and b==7) or (b==8 and a>=1 and a<=22):
   print("Карты говорят, что ты: Лев")

elif (a>=23 and a<=31 and b==8) or (b==9 and a>=1 and a<=22):
   print("Карты говорят, что ты: Дева")

elif (a>=23 and a<=30 and b==9) or (b==10 and a>=1 and a<=22):
   print("Карты говорят, что ты: Весы")

elif (a>=23 and a<=31 and b==10) or (b==11 and a>=1 and a<=21):
   print("Карты говорят, что ты: Скорпион")

elif (a>=22 and a<=30 and b==11) or (b==12 and a>=1 and a<=21):
   print("Карты говорят, что ты: Стрелец")

elif (a>=22 and a<=31 and b==12) or (b==1 and a>=1 and a<=19):
   print("Карты говорят, что ты: Козерог")

elif (a>=20 and a<=31 and b==1) or (b==2 and a>=1 and a<=18):
   print("Карты говорят, что ты: Водолей")

elif (a>=19 and a<=29 and b==2) or (b==3 and a>=1 and a<=20):
   print("Карты говорят, что ты: Рыбы")

print()

#3Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.
try:
    print("Хотители вы расшифровать номер?")
    o=(input("Да или Нет! "))
    if o.lower()=="да":
        print({o})
        a=int(input("Напишите число отв 1 до 7: "))
        if a>1 and a<8:
            if a==1:
                n="Понедельник"
            elif a==2:
                n="Вторник"
            elif a==3:
                n="Среда"
            elif a==4:
                n="Чеверг"
            elif a==5:
                n="Пятница"
            elif a==6:
                n="Суббота"
            elif a==7:
                n="Воскресенье"
            else: 
                n="Не правильное число"
            print(n)
        else: 
            print("Вы выбрали не правильный диапазон чисел!") 
    elif o.upper()=="НЕТ":
         print("К сожалению вы не захотели расшивроват число")
except:
    print("Программа закрыта")
print()



#2
#Спросить у пользователя 3 числа, если они окажуться положительными, то проверить могут ли они быть углами одного треугольника(сумма углов 180) и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний
print("Проверка на треугольник")
a=float(input("sisesta arv: "))
b=float(input("sisesta arv: "))
c=float(input("sisesta arv: "))
try:
    if a>0 and b>0 and c>0:
        if a+b+c==180:
            if a==b and b==c:
                print("равностороний треугольник")
            elif a==b or b==c or c==b:
                print("Равнобедренный треугольник")
            else:
                print("Разносторонего треугольника")
        else: 
            print("teie nubrit ie soobi")
except:
    print("Vahe sonad")
print()

#1Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное), если число положительное, то проверяет его 
#на  четность и нечетность.
try: 
    a=float(input("sisesta arv: "))
    if a>0:
        print("Positiivne")
        if a%2==0:
            print(f"{a} on paaris")
        else:
            print(f"{a} on paaritud")
    else:
            print("Negatiivmne")
except:
    print("Numbrid ei sobi")
  


