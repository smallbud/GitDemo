import requests
from bs4 import BeautifulSoup
from urllib import request

data = requests.get('http://www.baidu.com/')

soup = BeautifulSoup(data.text)
print(soup.prettify())