#test.py
import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 10, "name": "Tim", "views": 10000},
    {"likes": 10, "name": "Making REST API", "views": 700000},
    {"likes": 10, "name": "Becoming a Data Scientist", "views": 400000}  
]

  
for i in range(len(data)):
    response = requests.patch(BASE + "video/" + str(i), json=data[i])
    print(response.json())
    
   
input("press enter")
response = requests.delete(BASE + "video/1")
print(response)
input("press enter")

response = requests.put(BASE + "video/0")
print(response.json())
