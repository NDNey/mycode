#!/usr/bin/env python3
import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/getJson"

data = requests.get(URL).json()

print("this is an encyclopedia:")
for item in data:

    print(f"*Entry Creator : {item['user']} ")
    print(f"*{item['entry']} : {item['definition']}")
