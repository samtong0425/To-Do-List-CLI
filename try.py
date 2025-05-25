database = {
    "1": {
        "item": "",
        "status": "incomplete"
    },
    "2": {
        "item": "aa",
        "status": "complete"
    }
}
user_input = "1"
if database[user_input]['status'] == 'incomplete':
    print('11')
elif database[user_input]['status'] == 'complete':
    print('22')
