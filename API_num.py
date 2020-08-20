import requests
import json


# Обработка чисел из файла
# with open("example_dataset.txt") as f:
#     for num in f:
#         res = requests.get(api_url + num.strip() + "/math?json=true").text
#         print(json.loads(res)["text"] if json.loads(res)["found"] else 'Boring')

api_url = 'http://numbersapi.com/'
for num in input().split():
    res = requests.get(api_url + str(num) + "/math?json=true").text
    print(json.loads(res)["text"] if json.loads(res)["found"] else 'Boring')
