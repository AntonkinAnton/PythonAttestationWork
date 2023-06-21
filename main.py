from file_work import*
from notes_func import*
from os import system

system('cls||clear')

while True:
        Header('Главное меню')
        command = input("Введите команду (add, read, edit, delete, exit): ")
        match command:
            case "add":
                add_note()
            case "read":
                read_notes()
            case "edit":
                edit_note()
            case "delete":
                delete_note()
            case "exit":
                break
            case _:
                print("Некорректная команда. Попробуйте снова.")
