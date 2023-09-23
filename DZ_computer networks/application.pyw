import socket
import threading
import tkinter as tk
from tkinter import Scrollbar

# Функция для отправки сообщения
def send_message():
    message = entry.get()  # Получаем текст из поля ввода
    if message:
        chat_text.config(state=tk.NORMAL)  # Разрешаем редактирование текста
        chat_text.insert(tk.END, f"YOU: {message}\n")  # Добавляем сообщение отправителя
        chat_text.config(state=tk.DISABLED)  # Запрещаем редактирование текста
        entry.delete(0, tk.END)  # Очищаем поле ввода
        chat_text.yview(tk.END)  # Прокручиваем текст вниз, чтобы видеть последнее сообщение
        client.send(message.encode('utf-8'))  # Отправляем сообщение на сервер

# Функция для приема сообщений от сервера
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_text.config(state=tk.NORMAL)  # Разрешаем редактирование текста
            chat_text.insert(tk.END, message + '\n')  # Отображаем полученное сообщение
            chat_text.config(state=tk.DISABLED)  # Запрещаем редактирование текста
            chat_text.yview(tk.END)  # Прокручиваем текст вниз
        except Exception as e:
            print("An error occurred:", e)
            client.close()
            break

# Создаем главное окно
root = tk.Tk()
root.title("GigaGram")

# Создаем текстовое поле для чата с вертикальным скроллингом
chat_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_text.pack(fill=tk.BOTH, expand=True)

# Создаем поле для ввода текста
entry = tk.Entry(root)
entry.pack(fill=tk.BOTH, expand=True)

# Создаем кнопку для отправки сообщения
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

# Создаем вертикальный скроллбар и привязываем его к текстовому полю чата
scrollbar = Scrollbar(root, command=chat_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.place(relheight=1, relx=1)
chat_text.config(yscrollcommand=scrollbar.set)


# Подключение к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('IP', 55555))

# Запуск потоков для приема и отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()
