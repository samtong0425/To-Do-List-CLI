import sys
import os
import json

database = {}

try:
    with open("database.json", "r") as file:
        saved_database = json.load(file)
    for i, item in enumerate(saved_database.items(), 1):
        database.update({i: item[1]})
except FileNotFoundError:
    pass
except NameError:
    pass
except json.decoder.JSONDecodeError:
    pass


def display_list():
    global database
    os.system("clear")
    print(f"{'=' * 20} TO DO LIST {'=' * 20} ")
    for n, task in database.items():
        print(f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}")


'''
===============Business Logic===============
--Add Task
--Toggle Task Status
--Delete Task
'''

def add_task(new_task, database):
    new_id = len(database) + 1
    database[new_id] = {"item": new_task, "status": "incomplete"}
    return database

def toggle_task_status(id, database):
    if database[id]['status'] == 'incomplete':
        database[id].update({"status": "complete"})
    else:
        database[id].update({"status": "incomplete"})

def delete_task(id, database):
    deleted_item = database.pop(id)
    update_database = {}

    for i, item in enumerate(database.items(), 1):
        update_database.update({i: item[1]})

    database.clear()
    database.update(update_database)
    return deleted_item

'''
===============Sub-Menu UI===============
'''

def new_task():
    global database
    while True:
        display_list()
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
            display_list()
            print(f"\n{new_task.capitalize()} is added.")


def mark_complete():
    global database
    while True:
        
        display_list()
        print("\n----- MARK TASK COMPLETE -----")
        prompt = "MARK: Enter task ID (or 'q' to return): "
        id = input(prompt).strip().lower()
        print("-" * 30)

        if id in ["q", "quit"]:
            break

        try:
            id = int(id)
        except ValueError:
            print("Invalid Input")
            input("Press Enter to continue...")
            continue

        if id in database.keys():
            toggle_task_status(id, database)
            display_list()
            item, status = database[id].values()
            print(f"\n{id}: {item.capitalize()} - Status: {status.capitalize()}")
        else:
            print("Your selected item is not exit.")
            input("Press Enter to continue...")
            continue


def del_item():
    global database
    while True:
        display_list()
        print("\n----- DELETE TASK -----")
        delete_item = (
            input("DELETE: Enter task ID (or 'q' to return): ").strip().lower()
        )
        if delete_item in ["q", "quit"]:
            break
        try:
            delete_item = int(delete_item)
        except ValueError:
            print("Invalid Input")
            input("Press Enter to continue...")
            continue

        if delete_item in database.keys():
            id = int(delete_item)
            del_comfirm = (
                input(f"Do you confirm delete {database[id]['item']}? (y)es or no: ")
                .strip()
                .lower()
            )
            if del_comfirm in ["yes", "y"]:
                deleted_item = delete_task(id, database)
                display_list()
                print(f"\n{deleted_item['item'].capitalize()} is deleted.")

        else:
            print("Your selected item is not exit.")
            input("Press Enter to continue...")
            continue

'''
===============Main Menu UI===============
'''

def main():
    global database

    while True:
        display_list()
        print(f"\n{'=' * 21} MAIN MENU {'=' * 20} ")
        prompt = "\nCommand: (a)dd, (m)ark, (d)elete, (h)lep, (q)uit: "
        command = input(prompt).strip().lower()
        if command in ["a", "add"]:
            new_task()

        elif command in ["m", "mark"]:
            mark_complete()

        elif command in ["d", "delete"]:
            del_item()

        elif command in ["h", "help"]:
            os.system("clear")
            with open("help.txt") as help:
                print(f"{help.read()}\n")

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
