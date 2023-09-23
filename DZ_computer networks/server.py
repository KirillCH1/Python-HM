import socket
import threading

# Данные о подключении
host = 'IP'
port = 55555

# Запуск сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Списки клиентов и их Ники
clients = []
nicknames = []

# Отправка Сообщений Всем Подключенным Клиентам
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

# Обработка сообщений от Клиентов
def handle(client):
    while True:
        try:
            # Получить сообщение
            message = client.recv(1024).decode('utf-8')
            if message:
                # Трансляция сообщения с псевдонимом отправителя
                nickname = nicknames[clients.index(client)]
                broadcast(f'{nickname}: {message}'.encode('utf-8'), client)
        except:
            # Удаление и закрытие клиентов
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'), client)
            nicknames.remove(nickname)
            break

# Функция приема / прослушивания
def receive():
    while True:
        # Принять соединение
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Запросить И Сохранить псевдоним
        client.send('Введите ваш ник:'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Печатать И Транслировать Псевдоним
        print("{} присоединился!".format(nickname))
        broadcast("{} присоединился!".format(nickname).encode('utf-8'), client)
        client.send('Подключен к серверу!'.encode('utf-8'))

        # Начать обработку потока для Клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
