import requests

url = "https://api.meaningcloud.com/sentiment-2.1"

payload={
    'key': '97e69308224f8793edeb68616bc90c65',
    'txt': 'YOUR TEXT HERE',
    'lang': 'TEXT LANGUAGE HERE',  # 2-letter code, like en es fr ...
}

response = requests.post(url, data=payload)

print('Status code:', response.status_code)
print(response.json())