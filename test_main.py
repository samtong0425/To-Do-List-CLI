import main

def test_add_task():
    database = {}
    new_task = "Buy milk"
    main.add_task(new_task, database)
    print(database)
    assert len(database) == 1
    assert '1' in database
    assert database['1'] == {"item": "Buy milk", "status": "incomplete"}    

# test_add_task()