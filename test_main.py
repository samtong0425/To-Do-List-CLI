import main


def test_add_task():
    database = {}
    new_task = "Buy milk"
    main.add_task(new_task, database)
    print(database)
    assert len(database) == 1
    assert "1" in database
    assert database["1"] == {"item": "Buy milk", "status": "incomplete"}


def test_toggle_task_status():
    database = {"1": {"item": "Grocery shopping", "status": "incomplete"}}
    id = "1"
    assert database[id]["status"] == "incomplete"
    main.toggle_task_status(id, database)
    assert database[id]["status"] == "complete"
    main.toggle_task_status(id, database)
    assert database[id]["status"] == "incomplete"


def test_delete_task():
    database = {
        "1": {"item": "Grocery shopping", "status": "incomplete"},
        "2": {"item": "Pay bills", "status": "incomplete"},
        "3": {"item": "Schedule doctor's appointment", "status": "incomplete"},
        "4": {"item": "Walk the dog", "status": "incomplete"},
        "5": {"item": "Read a book", "status": "incomplete"},
    }
    id_str = "3"
    main.delete_task(id_str, database)
    assert len(database) == 4
    assert "5" not in database
    assert database["3"] == {"item": "Walk the dog", "status": "incomplete"}
