import json

def load_notes(NOTES_FILE):
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes, NOTES_FILE):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)