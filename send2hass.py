import time
from datetime import datetime
from requests import post


def change_state(entity_id, new_state):
    url = 'http://localhost:8123/api/states/' + entity_id

    state_data = {
        'state': new_state,
    }
    
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYTI0MzBkMmEyN2E0OTc1ODUyZmQ5NzQwNDA4YWQ0NSIsImlhdCI6MTU3OTA4NTMzMywiZXhwIjoxODk0NDQ1MzMzfQ.jrMlPWQEdjfGfHMvzKk0DTf2fx4CzMkYsmewk5bw5tk',
        'content-type': 'application/json',
    }
    print(entity_id, new_state)
    # response = post(url, headers=headers, json=state_data)
    # print(response.text)


  
