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


def display_list():
    global database
    os.system("clear")
    print(f"{'=' * 20} TO DO LIST {'=' * 20} ")
    for n, task in database.items():
        print(f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}")


def add_item():
    global database
    while True:
        display_list()
        print("\n----- ADD NEW TASK -----")
        add_item = input("ADD: Enter new task (or 'q' to return):").strip()
        print("-" * 25)
        if add_item in ["q", "quit"]:
            break
        elif not add_item:
            print("Input cannot be empty or contain only whitespace.")
            input("Press Enter to continue...")
            continue
        else:
            id = len(database) + 1
            database[id] = {"item": add_item, "status": "incomplete"}
            display_list()
            print(f"\n{add_item.capitalize()} is added.")


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
            if database[id]['status'] == 'complete':
                database[id].update({"status": "incomplete"})
            elif database[id]['status'] == 'incomplete':
                database[id].update({"status": "complete"})
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
                deleted_item = database.pop(id)
                update_debate = {}
                for i, item in enumerate(database.items(), 1):
                    update_debate.update({i: item[1]})
                database.clear()
                database = update_debate.copy()
                update_debate.clear()
                display_list()
                print(f"\n{deleted_item['item'].capitalize()} is deleted.")

        else:
            print("Your selected item is not exit.")
            input("Press Enter to continue...")
            continue


def main():
    global database

    while True:
        display_list()
        print(f"\n{'=' * 21} MAIN MENU {'=' * 20} ")
        prompt = "\nCommand: (a)dd, (m)ark, (d)elete, (h)lep, (q)uit: "
        command = input(prompt).strip().lower()
        if command in ["a", "add"]:
            add_item()

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


main()
