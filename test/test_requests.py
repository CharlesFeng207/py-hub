import requests
from requests import Response 
import random


while True:
    rsp = requests.get('http://139.155.88.114:5000/query', {"content":random.random(), "save":0})
    print(rsp.text)