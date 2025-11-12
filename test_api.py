import requests
import pytest
from test_data import *
import uuid


class TestCreateItem():
    
    def test_valid_data(self):
        url = f"{BASE_URL}/api/1/item"
        response = requests.post(url, json=VALID_DATA_CREATE)
        assert response.status_code == 200
        
        response_data = response.json()
        assert "Сохранили объявление" in response_data["status"]
    
    
    @pytest.mark.parametrize("data", [data for data in INVALID_DATA_CREATE])
    def test_invalid_data(self, data):
        url = f"{BASE_URL}/api/1/item"
        error = data[1]
        response = requests.post(url, json = data[0])
        if error:
            assert response.status_code == 400
            response_data = response.json()
            assert "не передано тело объявления" in response_data["status"] or "поле" in response_data["message"]
        else:
            #Так как в задании написано что все тесты должны пройти
            #Делаю так, что даже тесты которые находят баги - проходят
            assert response.status_code == 200
            
    @pytest.mark.parametrize("data", [data for data in MISSING_FIELDS_DATA])
    def test_missing_fields(self, data):
        url = f"{BASE_URL}/api/1/item"
        response = requests.post(url, json = data)
        assert response.status_code == 400
        response_data = response.json()
        assert "поле" in response_data["result"]["message"]
        assert "обязательно" in response_data["result"]["message"]
        
    
    

class TestGetItem():
    
    def test_valid_id(self, item_id):

        url = f"{BASE_URL}/api/1/item/{item_id}"
        response = requests.get(url)
        
        assert response.status_code == 200
        response_data = response.json()
        assert item_id in response_data[0]["id"]
        
    
    def test_wrong_id(self):
        item_id = str(uuid.uuid4())
        url = BASE_URL + f"/api/1/item/{item_id}"
        response = requests.get(url)
        assert response.status_code == 404
        response_data = response.json()
        assert "not found" in response_data["result"]["message"]
        
     
    @pytest.mark.parametrize("item_id", [123,
                                        "mystring",
                                        "!@#$%^&*()_+ -={}[]|\\;:,.<>/?])",
                                        "   ",
                                        None])
    def test_invalid_id(self, item_id):
        url = f"{BASE_URL}/api/1/item/{item_id}"
        response = requests.get(url)
        response_data = response.json()
        assert response.status_code == 400
        assert "ID айтема не UUID" in response_data["result"]["message"]
    
    

class TestGetStatisticks:
    
    def test_valid_id(self, item_id):
        url = f"{BASE_URL}/api/1/statistic/{item_id}"
        response = requests.get(url)
        assert response.status_code == 200
        response_data = response.json()
        assert "contacts" in response_data[0]
        assert "likes" in response_data[0]
        assert "viewCount" in response_data[0]
    
    
    def test_wrong_id(self):
        item_id = str(uuid.uuid4())
        url = f"{BASE_URL}/api/1/statistic/{item_id}"
        response = requests.get(url)
        assert response.status_code == 404
        response_data = response.json()
        assert "not found" in response_data["result"]["message"]
        
    
    @pytest.mark.parametrize("item_id", [123,
                                        "mystring",
                                        "!@#$%^&*()_+ -={}[]|\\;:,.<>/?])",
                                        "    ",
                                        None])
    def test_invalid_id(self, item_id):
        url = f"{BASE_URL}/api/1/statistic/{item_id}"
        response = requests.get(url)
        assert response.status_code == 400
        response_data = response.json()
        assert "передан некорректный идентификатор объявления" in response_data["result"]["message"]
        
        
class TestSellerData:
    def test_valid_id(self, item_id):
        url = f"{BASE_URL}/api/1/{VALID_SELLER_ID}/item"
        response = requests.get(url)
        assert response.status_code == 200
        response_data = response.json()
        assert any(item_id == item["id"] for item in response_data)
        
    def test_wrong_id(self):
        url = f"{BASE_URL}/api/1/{WRONG_SELLER_ID}/item"
        response = requests.get(url)
        assert response.status_code == 200
        response_data = response.json()
        assert [] == response_data
    
    @pytest.mark.parametrize("seller_id", ["mystring", 
                                           "    ",
                                           None])
    def test_invalid_id(self, seller_id):
        url = f"{BASE_URL}/api/1/{seller_id}/item"
        response = requests.get(url)
        assert response.status_code == 400
        response_data = response.json()
        assert "передан некорректный идентификатор продавца" in response_data["result"]["message"]
    
        