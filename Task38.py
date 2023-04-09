
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import json
import os

def Create_contact() -> dict:
    return dict(
        first_name = input('Введите имя: ').lower(),
        second_name = input('Введите фамилию: ').lower(),
        contacted = input('Введите номер телефона: ')
    )

def Save_contact(list_contact: list) -> None:
    with open('contacted.txt', 'w') as data:
        json.dump(list_contact, data)

def Find_contact(list_contact: list) -> list:
    search = input("Введите Имя, Фамилию или номер: ").lower()
    found = []
    temp:int = 0
    for a in list_contact:
        if search in (a['first_name'],a['second_name'],a['contacted']):
            found.append(a)
            temp += 1
            print(f"{temp}. " + a['first_name'].capitalize()+ " " + a['second_name'].capitalize() + " " + a['contacted'])
    if len(found) == 0:
        print("Совпадений не найдено")
        return None
    return found

def Delete_contact(list_contact: list) -> list:
    try:
        dellet = Find_contact(list_contact)
        if dellet == None:
            return
        if len(dellet) == 1:
            choice = int(input("Удалить файл ? (1 - да) (2 - нет)"))
            if choice == 1:
                for f in list_contact:
                    if f == dellet[0]:
                        del f['first_name']
                        del f['second_name']
                        del f['contacted']
                        with open('contacted.txt', 'w') as data:
                            list_contact = list(filter(None,list_contact ))
                            json.dump(list_contact, data)
                            print("Файл удалён")
            else:
                return
        else:
            print(f"Найдено \"{len(dellet)}\" ")
            number_del = int(input("Введите номер элемента который надо удалить: "))
            for f in list_contact:
                if dellet[number_del-1] == f:
                    del f['first_name']
                    del f['second_name']
                    del f['contacted']
                    with open('contacted.txt', 'w') as data:
                        list_contact = list(filter(None,list_contact ))
                        json.dump(list_contact, data)
                        print("Файл удалён")
    except:
        print("Ошибка ввода")

def Change_contact(list_contact: list):
    change = Find_contact(list_contact)
    if change == None : 
        return
    vo = int(input("Хотите изменить контакт? (1 - да) (2 - нет) "))
    if vo == 2 : return
    if len(change) == 1:
        for a in list_contact:
            if a == change[0]:
                a1 = input('Введите имя: ').lower()
                a2 = input('Введите фамилию: ').lower()
                a['first_name'] = a1
                a['second_name'] = a2
                a['contacted'] = input('Введите номер телефона: ')
                print("Файл изменён")
    else:
        print(f"Найдено \"{len(change)}\" ")
        number_del = int(input("Введите номер элемента который надо удалить: "))
        for f in list_contact:
            if change[number_del-1] == f:
                pass


def Loading_data():
    if os.path.isfile("contacted.txt"):
        with open('contacted.txt', 'r') as data:
            list_contact = json.load(data)
    else :
        with open('contacted.txt', 'w+') as data:
            list_contact = []
            
    return list_contact

def Print_contact(list_contact: list):
    temp = 0
    for contact in list_contact:
        temp += 1
        print(f"№{temp}")
        print("Имя    : " + contact['first_name'].capitalize())
        print("Фамилия: " + contact['second_name'].capitalize())
        print("Телефон: " + contact['contacted'])

def Menu():
    while True:
        clear = lambda: os.system('clear')
        clear()
        try:
            print("1. Показать все контакты")
            print("2. Найти  контакт")
            print("3. Добавить контакт")
            print("4. Изменить контакт")
            print("5. Удалить контакт")
            print("0. Выход")
            command = int(input("Введите цифру меню: "))
            if command < 7:
                print(f"{command}")
                clear()
                return command
            else:
                1/0
        except:
            clear()
            print("Ошибка, введите пункт меню!")
            input()

def main():
    while True:
        command = Menu()
        contact = Loading_data()
        if command == 1:
            Print_contact(contact)
            input("Введите любое значение чтобы продолжить: ")
        
        if command == 2:
            Find_contact(contact)
            input("Введите любое значение чтобы продолжить: ")

        if command == 3:
            contact.append(Create_contact())
            Save_contact(contact)
            input("Введите любое значение чтобы продолжить: ")
        
        if command == 4:
            Change_contact(contact)
            Save_contact(contact)
            input("Введите любое значение чтобы продолжить: ")

        if command == 5:
            Delete_contact(contact)
            
            input("Введите любое значение чтобы продолжить: ")

        if command == 0:
            break

main()
