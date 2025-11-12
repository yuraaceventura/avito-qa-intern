import pytest
import requests
from test_data import VALID_DATA_CREATE, BASE_URL, VALID_SELLER_ID

@pytest.fixture(scope="session")
def item_id():
    url = f"{BASE_URL}/api/1/item"
    response = requests.post(url, json=VALID_DATA_CREATE)
    response_data = response.json()
    status = response_data["status"]
    id = status.split(" - ")[1].strip()
    for _ in range(10):
        print(id)
    yield id

            
    
# @pytest.fixture(scope="session")
# def teardown():
#     yield
    
#     url = f"{BASE_URL}/api/2/{VALID_SELLER_ID}/item"
#     delete_url = f"{BASE_URL}/api/2/item/"
#     response = requests.get(url)
#     response_data = response.json()[0]
    
#     for item in response_data:
#             id = item["id"]
#             requests.delete(f"{delete_url}{id}")
            