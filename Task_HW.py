# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:
# 385916 -> yes
# 123456 -> no

print("Введите число из 6 символов")
n = int(input())
m = n
a = 0
while n > 0:
    if n > 0:
        n = n // 10
        a = a + 1
if a != 6:
    print("Данные введены не корректно! Попробуйте еще раз!")
else:
    sum1 = 0
    sum2 = 0
    a = 0
    while m > 0:
        if a < 3:
            sum2 += m % 10
        else:
            sum1 += m % 10
        a = a + 1
        m = m // 10

    if sum1 == sum2:
        print("Ваш билет счастливый!!! Поздравляем!!!")
    else:
        print("Увы. Ваш билет не счастливый((")




# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите длину шоколадки в дольках:")
n = int(input()) 
print("Введите высоту шоколки в дольках:")
m = int(input())
print("Введите сколько долек ВЫ желаете отломить:")
print("Но помните: у вас всего ОДНА попытка!!!")
x = int(input())
size = n * m
if x == size:
    print("Вы указали размер всей плитки! Деление не возможно!")
elif x > size:
    print("Количество желаемых плиток больше размера шоколадки! ВЫ жадина)))")
else:
    if n % 2 == 0 and m % 2 == 0:
        if x % n == 0 or x % m == 0:
            print("Ура! У вас получилось")
        else:
            print("Не в этот раз!")
    elif n % 2 == 0 or m % 2 == 0:
        if  x % n == 0 or x % m == 0:
            print("Ура! У вас получилось")
        else:
            print("Не в этот раз!")
    else:
        if  x % n == 0 or x % m == 0:
            print("Ура! У вас получилось")
        else:
            print("Не в этот раз!")
