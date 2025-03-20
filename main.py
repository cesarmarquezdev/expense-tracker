"""$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20"""

from repository import get_data
from datetime import datetime
from services import add_expense, delete_expense

data = get_data


def show_menu():
    return """\n
1 update an expense.
2 delete an expense.
3 view all expenses.
4 view a summary of all expenses.
5 view a summary of expenses for a specific month (of current year).
6 end program 
    """


def show_expenses():
    expenses = get_data()
    if not expenses:
        print("It's no expenses")
    else:
        for expense in expenses:
            print(
                f"ID: {expense['id']} | Description: {expense['description']} | Date: {expense['date']} | Amount: ${expense['amount']}"
            )


def get_valid_id(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter a valid number.")


def expense_manager():
    while True:
        print(show_menu())
        option = input("select a option (1, 2, 3, 4 , 5 o 6): ").strip()

        if option not in {"1", "2", "3", "4", "5", "6"}:
            print("Option it's no valid, Enter a valid option")
            continue

        option = int(option)

        if option == 1:
            while True:
                description = input("Type a descripcion for the expense: ").strip()
                if description:
                    amount = int(input("Type the amount of de expense: "))
                    tasks = get_data()
                    actual_date = datetime.today().strftime("%Y-%m-%d")
                    task_id = len(tasks) + 1
                    new_expense = {
                        "id": task_id,
                        "description": description,
                        "date": actual_date,
                        "amount": amount,
                    }
                    add_expense(new_expense)
                    print(
                        f"ID: {new_expense['id']} | Description: {new_expense['description']} | Date: {new_expense['date']} | Amount: ${new_expense['amount']}"
                    )
                else:
                    print("the descripcion can be empty")

                if (
                    input("do you want add another expense? (s/n): ").strip().lower()
                    != "s"
                ):
                    break

        elif option == 2:
            while True:
                show_expenses()
                task_id = get_valid_id("Enter the ID of the task to be deleted: ")
                delete_expense(task_id)
                print("expense delete succefully.")

                if (
                    input("Do you want to delete another expense? (s/n): ")
                    .strip()
                    .lower()
                    != "s"
                ):
                    break
        elif option == 3:
            show_expenses()
            if input("end? (s/n): ").strip().lower() != "s":
                break

        elif option == 4:
            while True:
                data = get_data()
                total = 0
                for amount in data:
                    total += amount["amount"]
                    
                print(f"the summary of all expenses is: ${total} ")
                if input("end? (s/n): ").strip().lower() != "n":
                    break

        elif option == 5:
            while True:
                month = (input("Pls type the month (YYYY-MM) : "))
                data = get_data()
                total = 0
                for expense in data:
                    if expense["date"].startswith(month):
                        total += expense["amount"]
                    
                print(f"the summary of all expenses is: ${total} ")
                if input("end? (s/n): ").strip().lower() != "n":
                    break

        elif option == 6:
            print("see you later my friend")
            break


if __name__ == "__main__":
    expense_manager()
