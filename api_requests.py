import requests

def post_data(count):
    response = requests.post('http://0.0.0.0:80/post_num', params={'questions_num': count})
    print(response.json())

post_data(100)
