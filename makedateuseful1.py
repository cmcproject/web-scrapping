import requests
from bs4 import BeautifulSoup

url = 'http://itmapro.herokuapp.com/'
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

h2 = soup.find_all('h2')[0]

print(h2)
print(h2.text)
