#Выведите все элементы, которые меньше 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for list in a:
    if list < 5:
        print(list)
    else:
        continue    

#вернуть список, который состоит из элементов, общих для этих двух списков
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]

for list in a:
    if list in b:
        c.append(list)

print(c)


#Напишите программу для слияния нескольких словарей в один

dic = {1:"Tom", 2:"Dick", 3:"Lucy", 4:"Bob"}
dic2 = {23: "Home", 25:"Car", 56:"Work"}

dic.update(dic2)
print(dic)

#############################
# функция угадывает время года по номеру месяца

def season():
    seas = int(input("Enter number of month: "))
    if 0<season<=12:
        if 1<=seas<=2 or seas ==12:
            print("It`s a winter")
        elif  3<=seas<=5:
            print("It`s a spring")
        elif  6<=seas<=8:
            print("It`s a summer")
        elif 9<=seas<=11:
            print("It`s a fall")   
    else:
        print("Incorrect value of variable")                 

season()
####################################################################
# Функция расчитывае доход от вклада
def bank ():
    sum = float(input("Enter a sum of deposit: "))
    number_of_years = float(input("Enter numbers of years: "))

    res_sum = float((sum + (sum /100 * 10)) * number_of_years)
    print(res_sum)


bank()     


#########################################################################

#Выведите первый и последний элемент списка

some_list = [1,2,6,8,7,9,7,1]

print(some_list[0])
print(some_list[-1])

#####################################################################

# Напишите программу, которая выводит чётные числа из заданного списка и 
# останавливается, если встречает число 237

import  random 

numbers = []
for i in range(10):
    numbers.append(int(random.random() * 1000))

print(numbers)

for i in numbers:
    if i % 2 ==0:
        print(i)
    else:
        continue

    if i ==237:
        break
###########################################################

# разделить 3х значное число на 3 отдельных числа

user_number = int(input("Введите 3х значное число: ")) #123

if (user_number / 1000) < 1 and (user_number / 100)>1:

    num_1 = int(user_number / 100) #1
    num_1_1 = int(user_number%100) #23

    num_2 = int(num_1_1 / 10) #2
    num_2_2 = int(num_1_1 % 10)

    print("{}, {}, {}.".format(num_1, num_2, num_2_2))

else:
    print("Введено не 3х значное число")


