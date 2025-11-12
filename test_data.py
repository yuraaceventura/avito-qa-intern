BASE_URL = "https://qa-internship.avito.com"

VALID_SELLER_ID = 546753
WRONG_SELLER_ID = 233445
VALID_DATA_CREATE = {
    "sellerID": 546753,
    "name": "testItem1",
    "price": 9999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }
}

INVALID_DATA_CREATE = [
    [{
    "sellerID": "",
    "price": 999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }}, True],
    [{
    "sellerID": "546753",
    "name": "testItem2",
    "price": 999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }}, True],
    [{
    "sellerID": "null",
    "name": "testItem3",
    "price": -999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }}, True],
    [{
    "sellerID": 546753,
    "name": "testItem4",
    "price": 999,
    "statistics": {
        "likes": -1,
        "viewCount": -1,
        "contacts": -1
    }}, False],
    [{
    "sellerID": 546753,
    "name": "testItem5",
    "price": -9999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }}, False],
]

MISSING_FIELDS_DATA = [
    {
    "sellerID": 546753,
    "name": "testItem4",
    "statistics": {
        "likes": 1,
        "viewCount": 4,
        "contacts": 2
    }},
    {
    "sellerID": 546753,
    "name": "testItem5",
    "price": 999,
    "statistics": {
        "viewCount": 4,
        "contacts": 2
    }},
    {
    "sellerID": 546753,
    "name": "testItem5",
    "price": -9999,
    "statistics": {
        "likes": 1,
        "contacts": 2
    }},
    {
    "sellerID": 546753,
    "name": "testItem5",
    "price": -9999,
    "statistics": {
        "likes": 1,
        "viewCount": 4,
    }}]