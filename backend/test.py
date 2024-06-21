import requests

Base = "http://127.0.0.1:5000/"

response = requests.get(Base + "helloworld/tim")

print(response.json())