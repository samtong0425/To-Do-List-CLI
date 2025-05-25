from tabulate import tabulate

database = [{"id": "1", "item": "Grocery shopping","status": "incomplete"}, {"id": "2", "item": "Pay bills", "status": "incomplete"},
            {"id": "3", "item": "Schedule doctor's appointment", "status": "incomplete"}]



print(tabulate(database, tablefmt="grid"))

database = {
    "1": {
        "item": "Grocery shopping",
        "status": "incomplete"
    },
    "2": {
        "item": "Pay bills",
        "status": "incomplete"
    },
    "3": {
        "item": "Schedule doctor's appointment",
        "status": "incomplete"
    },
    "4": {
        "item": "Walk the dog",
        "status": "incomplete"
    },
    "5": {
        "item": "Read a book",
        "status": "incomplete"
    },
    "6": {
        "item": "Clean the kitchen",
        "status": "incomplete"
    },
    "7": {
        "item": "Respond to emails",
        "status": "incomplete"
    },
    "8": {
        "item": "Plan weekend getaway",
        "status": "complete"
    },
    "9": {
        "item": "Learn a new recipe",
        "status": "complete"
    },
    "10": {
        "item": "gym",
        "status": "incomplete"
    }
}

table_database = []
for i, item in enumerate(database.items(), 1):
    table_database.append({"id" :str(i)})
    table_database[i-1].update(item[1])

print(table_database)
print(tabulate(table_database, tablefmt="grid"))
