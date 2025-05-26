import sys
import os
import json
from tabulate import tabulate



"""
===============Open exiting list if any===============
"""

Database = {}

try:
    with open("database.json", "r") as file:
        database = json.load(file)
except FileNotFoundError:
    pass
except NameError:
    pass
except json.decoder.JSONDecodeError:
    pass


"""
===============Display List===============
"""


def display_list(database):
    os.system("clear")
    print(f"{'=' * 20} TO DO LIST {'=' * 20} ")
    table_database = []
    for i, item in enumerate(database.items(), 1):
        table_database.append({"id" :str(i)})
        table_database[i-1].update(item[1])
    print(tabulate(table_database, tablefmt="grid"))
    # for n, task in database.items():
    #     print(f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}")


"""
===============Business Logic===============
--Add Task
--Toggle Task Status
--Delete Task
"""


def add_task(new_task, database):
    new_id_int = len(database) + 1
    new_id_str = str(new_id_int)
    database[new_id_str] = {"item": new_task, "status": "incomplete"}


def toggle_task_status(id_str, database):
    if database[id_str]["status"] == "incomplete":
        database[id_str].update({"status": "complete"})
    else:
        database[id_str].update({"status": "incomplete"})


def delete_task(id_str, database):
    deleted_item = database.pop(id_str)
    update_database = {}

    for i, item in enumerate(database.items(), 1):
        update_database.update({str(i): item[1]})

    database.clear()
    database.update(update_database)
    return deleted_item


"""
===============Sub-Menu UI===============
"""


def new_task_menu(database):
    while True:
        display_list(database)
        print("\n----- ADD NEW TASK -----")
        new_task = input("ADD: Enter new task (or 'q' to return):").strip()
        print("-" * 25)
        if new_task in ["q", "quit"]:
            break
        elif not new_task:
            print("Input cannot be empty or contain only whitespace.")
            input("Press Enter to continue...")
            continue
        else:
            add_task(new_task, database)
            display_list(database)
            print(f"\n{new_task.capitalize()} is added.")


def mark_complete_menu(database):
    while True:
        display_list(database)
        print("\n----- MARK TASK COMPLETE -----")
        prompt = "MARK: Enter task ID (or 'q' to return): "
        id_str = input(prompt).strip().lower()
        print("-" * 30)

        if id_str in ["q", "quit"]:
            break

        if id_str in database.keys():
            toggle_task_status(id_str, database)
            display_list(database)
            item, status = database[id_str].values()
            print(f"\n{id_str}: {item.capitalize()} - Status: {status.capitalize()}")
        else:
            print("Your selected item is not exit.")
            input("Press Enter to continue...")
            continue


def del_item_menu(database):
    while True:
        display_list(database)
        print("\n----- DELETE TASK -----")
        delete_item = (
            input("DELETE: Enter task ID (or 'q' to return): ").strip().lower()
        )
        if delete_item in ["q", "quit"]:
            break

        if delete_item in database.keys():
            del_comfirm = (
                input(
                    f"Do you confirm delete {database[delete_item]['item']}? (y)es or no: "
                )
                .strip()
                .lower()
            )
            if del_comfirm in ["yes", "y"]:
                deleted_item = delete_task(delete_item, database)
                display_list(database)
                print(f"\n{deleted_item['item'].capitalize()} is deleted.")

        else:
            print("Your selected item is not exit.")
            input("Press Enter to continue...")
            continue


"""
===============Main Menu UI===============
"""


def main():
    global database

    while True:
        display_list(database)
        print(f"\n{'=' * 21} MAIN MENU {'=' * 20} ")
        prompt = "\nCommand: (a)dd, (m)ark, (d)elete, (h)lep, (q)uit: "
        command = input(prompt).strip().lower()
        if command in ["a", "add"]:
            new_task_menu(database)

        elif command in ["m", "mark"]:
            mark_complete_menu(database)

        elif command in ["d", "delete"]:
            del_item_menu(database)

        elif command in ["h", "help"]:
            os.system("clear")
            with open("help.txt") as help:
                print(f"{help.read()}\n")
            input("Press Enter to continue...")
            

        elif command in ["q", "quit"]:
            with open("database.json", "w") as file:
                json.dump(database, file, indent=4)
            os.system("clear")
            sys.exit("Have a nice day!")

        else:
            os.system("clear")
            print("Please enter valid command.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
