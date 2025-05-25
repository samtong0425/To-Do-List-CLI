import sys
import os


def main():
    database = {
        1: {"item": "eat lunch", "status": "incomplete"},
        2: {"item": "eat dinner", "status": "incomplete"},
    }

    while True:
        for n, task in database.items():
            print(f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}")

        command = (
            input("\nCommand (a/add, m/mark, d/delete, h/help, q/quit): ")
            .strip()
            .lower()
        )
        if command in ["a", "add"]:
            while True:
                add_item = input("Add item: ")
                if add_item in ["q", "quit"]:
                    os.system("clear")
                    break
                else:
                    os.system("clear")
                    id = len(database) + 1
                    database[id] = {"item": add_item, "status": "incomplete"}
                    for n, task in database.items():
                        print(
                            f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}"
                        )
                    print(f"\n{add_item.capitalize()} is added.")

        elif command in ["m", "mark"]:
            while True:
                status_update = input("Item mark as complete: ")
                if status_update in ["q", "quit"]:
                    os.system("clear")
                    break
                else:
                    os.system("clear")
                    id = int(status_update)
                    database[id].update({"status": "complete"})
                    item, status = database[id].values()
                    for n, task in database.items():
                        print(
                            f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}"
                        )
                    print(
                        f"\n{id}: {item.capitalize()} - Status: {status.capitalize()}"
                    )

        elif command in ["d", "delete"]:
            while True:
                delete_item = input("Delete item: ")
                if delete_item in ["q", "quit"]:
                    os.system("clear")
                    break
                else:
                    os.system("clear")
                    id = int(delete_item)
                    deleted_item = database.pop(id)
                    update_debate = {}
                    for i, item in enumerate(database.items(), 1):
                        update_debate.update({i: item[1]})
                    database.clear()
                    database = update_debate.copy()
                    update_debate.clear()
                    for n, task in database.items():
                        print(
                            f"{n}: {task['item'].capitalize()} - {task['status'].capitalize()}"
                        )
                    print(f"\n{deleted_item['item'].capitalize()} is deleted.")

        elif command in ["q", "quit"]:
            os.system("clear")
            sys.exit("Have a nice day!")

        elif command in ["h", "help"]:
            os.system("clear")
            with open("help.txt") as help:
                print(f"{help.read()}\n")

        else:
            os.system("clear")
            print("Please enter valid command.")


main()
