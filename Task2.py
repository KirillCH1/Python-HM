# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

while True:
     try:
         number = float(input("Пожалуйста, введите целое число: "))
         break
     except ValueError:
         print("Это не целое число. Попробуйте снова...")
sum = 0
number = str(number)

for i in range(len(number)):
    if number[i] != '.':
        sum += int(number[i])
i += i
print(f'Сумма цифр числа равна: {sum}')
