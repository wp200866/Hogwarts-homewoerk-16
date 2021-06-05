import requests

# r = requests.get('http://www.baidu.com')
r = requests.post('http://www.baidu.com', data={'key':'value'})
print(r.text)