import requests
from bs4 import BeautifulSoup

site_map = 'https://www.pngmart.com/sitemap.xml/'
response = requests.get(site_map)

xml = response.text
soup = BeautifulSoup(xml, 'html.parser')

site_maps = []
for loc in soup.find_all('loc'):
    url = loc.text
    if 'post-sitemap' in url:
        site_maps.append(url)

site_map_1 = site_maps[0]

response = requests.get(site_map_1)
soup = BeautifulSoup(response.text, 'html.parser')

master_list = []
for loc in soup.find_all('loc'):
    url = loc.text
    master_list.append(url)

for image_url in master_list:
    if response.status_code == 200:
        response = requests.get(image_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        png_url = soup.find('a', {'class': 'download'})['href']

        image = requests.get(png_url)
        image_title = image_url.split('/')[-1] + '-' + png_url.split('/')[-1]

        with open(image_title, 'wb') as file:
            file.write(image.content)
    break

# digital ocean
