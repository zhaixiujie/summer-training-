import requests

r=requests.get('https://api.github.com/user',auth=('xxsfno@126.com','xx971125'))
print(r.text)