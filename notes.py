from file_work import*
from notes_func import*
from os import system

system('cls||clear')

NOTES_FILE = "notes.json"
header('Записная книжка')
while True:
        header('Главное меню')
        command = input("Введите команду (help для вывода доступных команд): ")
        print()
        match command.lower():
            case "help":
                header('Доступные команды')
                show_commands()
            case "add":
                header('Добавление заметки')
                add_note(NOTES_FILE)
            case "read":
                header('Просмотр и поиск по дате')
                read_notes(NOTES_FILE)
            case "edit":
                header('Редактирование заметки')
                edit_note(NOTES_FILE)
            case "delete":
                header('Удаление заметки')
                delete_note(NOTES_FILE)
            case "exit":
                print("До скорой встречи!\n")
                break
            case _:
                print("Некорректная команда. Попробуйте снова (help - для вывода доступных команд)")
