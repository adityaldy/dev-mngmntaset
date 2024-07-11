import requests

url = "https://asset-sentosa.someah.id/"
response = requests.get(url)
print(response.headers)
