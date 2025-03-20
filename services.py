import json
from repository import get_data


FILE_PATH = r"C:\Users\cesar\OneDrive\Python\proyect_spences\db_expences.json"


def add_expense(new_expense: dict) -> bool:
    if not new_expense:
        print("Invalid task description, please enter a valid one.")
        return False

    data = get_data()

    data.append(new_expense)

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("✅ Expence save succefully.")  # Asegurar que el archivo se escribió
        return True
    except Exception as e:
        print(f"❌ fail in save data: {e}")
        return False


def delete_expense(expense_id: int) -> bool:
    data = get_data()

    for expense in data:
        if expense["id"] == expense_id:
            data.remove(expense)
            print("delete succefully.")
            break
    else:
        print("expense not founded.")
        return False

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ fail: {e}")
        return False
