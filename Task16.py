# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X 
# n = 5
# 1 2 3 4 5
# x = 3 -> 1

try:
    N = int(input('Введите количество элементов N: '))
    list_nuber = list(map(int, input("Введите элементы списка: ").split()))
    if len(list_nuber) != N:
        print('Введенно неверное количество элементов!')
    else:
        X = int(input('Введите число которое необходимо найти: '))
        count = 0
        for i in range(N):
            if list_nuber[i] == X:
                count += 1
        print(f'Число {X} встречается в списке A {count} раз') 
except:
    print('Значение не должно содержать буквы')
