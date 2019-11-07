import time
from datetime import datetime
from requests import post


def change_state(entity_id, new_state):
    url = 'http://localhost:8123/api/states/' + entity_id

    state_data = {
        'state': new_state,
    }
    
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyOWUzYjcwZGZkMTE0NzQ2YjFkOTU2YmJiODQ4NzNmOSIsImlhdCI6MTU3Mjk1OTc1MCwiZXhwIjoxODg4MzE5NzUwfQ.dG8UmC0FlAdv4xCEf3LdK9OGvDx3AIcnOzVbVre_b2w',
        'content-type': 'application/json',
    }
   
    response = post(url, headers=headers, json=state_data)
    print(response.text)


  
#    change_state('light.l008', 'on')
#   self.pushButton_90.clicked.connect(lambda:lightsclick(self.pushButton_90,'l008'))

#lights = {'l008':1, 'l001':1, 'l004':1,'l011':1}

# def lightsclick(button,lname):
#     entity_id = 'light.'+lname
#     if lights[lname] == 1:
#         button.setStyleSheet("background-color: rgb(255, 255, 255);")
#         new_state='off'    
#         lights[lname] = 0
#     else:
#         button.setStyleSheet("background-color: rgb(0, 255, 0);")
#         new_state='on'    
#         lights[lname] = 1
#     change_state(entity_id, new_state)