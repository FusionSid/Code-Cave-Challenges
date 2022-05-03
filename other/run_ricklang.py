import requests


with open("file_name.rickroll") as f:
    data = f.read()

api_link = "https://whyapi.fusionsid.xyz/api/ricklang"

data = {
    "code" : data,
    "language" : "rickroll-lang"
}
response = requests.post(api_link, json=data).json()
print(response["output"])