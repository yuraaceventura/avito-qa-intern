import uuid
from test_data import *
import requests
print(str(uuid.uuid4()))

def test_valid_id():
        item_id = "fe094735-58aa-42c4-9dd5-8f8b6fd56dd0"
        url = BASE_URL + f"/api/1/item/{item_id}"
        response = requests.get(url)
        print(response.status_code)
        print(response.json())

        
    
def test_wrong_id():
        id = str(uuid.uuid4())
        url = BASE_URL + f"/api/1/item/{id}"
        response = requests.get(url)
        print(response.status_code)
        print(response.json())

def test_invalid_id(id):
        url = BASE_URL + f"/api/1/item/{id}"
        response = requests.get(url)
        response_data = response.json()
        print(response_data)

for i in ["",
                                    123,
                                    "mystring",
                                    r"""!@#$%^&*()_+ -={}[]|\\;:'",.<>/?"])"""]:
    test_invalid_id(i)
    print("-------")

test_valid_id()
test_wrong_id()