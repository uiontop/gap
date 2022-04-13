import requests


data = {
    'content':'token here'
}
while True:
    v = requests.post(url='http://127.0.0.1:8888/webhook/token', json=data)
    print(v.status_code)