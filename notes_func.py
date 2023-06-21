from file_work import*
import datetime

def header(message = "\n"):
    print(message.center(70, '='), '\n')


def add_note(NOTES_FILE):
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().isoformat()
    
    confirm = input("Данные введены верно? y/n:  ")
    if confirm.lower() == "y":
        notes = load_notes(NOTES_FILE)
        note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
        }
        notes.append(note)
        save_notes(notes, NOTES_FILE)
        print("Заметка успешно сохранена\n")
    else: 
        print("Создание заметки отменено\n")


def read_notes(NOTES_FILE):
    notes = load_notes(NOTES_FILE)
    if len(notes) == 0:
        print("Нет доступных заметок\n")
        return

    filter_option = input(
        "Выберите опцию фильтрации (1 - по всем заметкам, 2 - по дате): ")
    if filter_option == "1":
        filtered_notes = notes
    elif filter_option == "2":
        filter_date = input(
            "Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
        try:
            filter_date = datetime.datetime.strptime(
                filter_date, "%Y-%m-%d").date()
            filtered_notes = [note for note in notes if datetime.datetime.fromisoformat(
                note["timestamp"]).date() == filter_date]
        except ValueError:
            print("Некорректный формат даты.\n")
            return
    else:
        print("Некорректная опция фильтрации.\n")
        return

    if len(filtered_notes) == 0:
        print("Нет заметок, удовлетворяющих выбранной опции фильтрации.\n")
    else:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()


def edit_note(NOTES_FILE):
    note_id = input("Введите ID заметки для редактирования: ")
    notes = load_notes(NOTES_FILE)
    for note in notes:
        if note["id"] == int(note_id):
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            confirm = input("Данные введены верно? y/n:  ")
            if confirm.lower() == "y":
                note["title"] = new_title
                note["body"] = new_body
                note["timestamp"] = datetime.datetime.now().isoformat()
                save_notes(notes, NOTES_FILE)
                print("Заметка успешно отредактирована\n")
                return
            else:
                print("Редактирование заметки отменено\n")
                return
    print("Заметка с указанным ID не найдена\n")


def delete_note(NOTES_FILE):
    note_id = input("Введите ID заметки для удаления: ")
    notes = load_notes(NOTES_FILE)
    for note in notes:
        if note["id"] == int(note_id):
            notes.remove(note)
            save_notes(notes, NOTES_FILE)
            print("Заметка успешно удалена\n")
            return
    print("Заметка с указанным ID не найдена\n")

def show_commands():
    print(" add  - Добавить новую заметку\n read  - Вывод всех заметок или поиск по дате\n edit  - Редактирование заметки (выбор по ID)\n delete  - Удаление заметки (выбор по ID)\n exit  - Выход из программы\n")
