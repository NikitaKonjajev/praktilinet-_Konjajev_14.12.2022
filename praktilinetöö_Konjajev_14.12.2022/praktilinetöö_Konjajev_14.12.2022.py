from random import *
from math import *

#2
#Спросить у пользователя 3 числа, если они окажуться положительными, то проверить могут ли они быть углами одного треугольника(сумма углов 180) и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).
a=float(input("sisesta arv: "))
b=float(input("sisesta arv: "))
c=float(input("sisesta arv: "))
try:
    if (a+b+c)>0:
        print("sobib")




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
  


