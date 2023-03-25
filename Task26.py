#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def DegreeNumber(a,i) :
    if i == 1:
        return a
    return a * DegreeNumber(a,i-1)

try:
    a = int(input('Введите число:'))
    b = int(input('Введите степень числа:'))
    i =int(0)
    print(f'\"{a}\" в степени \"{b}\" равно {DegreeNumber(a,b)}')
    
except:
    print('Ошибка ввода')
