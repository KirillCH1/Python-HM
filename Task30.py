
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


try:
    datumPoint = int(input("Введите число отчета: "))
    progression = int(input("Введите число прогрессии: "))
    numberElements = int(input("Введите количество элементов: "))
    for i in range(numberElements):
        print(f"{datumPoint + i * progression}",end =" ")

except:
    print('Ошибка,введите целое число!')
