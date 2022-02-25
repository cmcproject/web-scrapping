from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.youtube.com/c/ElrondNetwork/videos')
driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span').click()

for _ in range(1):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
videos = soup.find_all('div', {'id': 'dismissible'})

master_list = []
for video in videos:
    data_dict = {}
    data_dict['title'] = video.find('a', {'id': 'video-title'}).text
    data_dict['video_url'] = 'https://www.youtube.com/' + video.find('a', {'id': 'video-title'})['href']
    meta = video.find('div', {'id': 'metadata-line'}).find_all('span')
    data_dict['views'] = meta[0].text
    data_dict['video_age'] = meta[1].text

    master_list.append(data_dict)

yt_df = pd.DataFrame(master_list)


def convert_views(df):
    if 'K' in df['views']:
        views = float(df['views'].split('K')[0]) * 1000
    elif 'M' in df['views']:
        views = float(df['views'].split('M')[0]) * 1000000

    return views


yt_df['CLEAN_VIEWS'] = yt_df.apply(convert_views, axis=1)
yt_df['CLEAN_VIEWS'] = yt_df['CLEAN_VIEWS'].astype(int)

yt_df.to_csv('output.csv')

# # Get data from each video
# driver.get(yt_df['video_url'][1])
# time.sleep(1)
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# video_views = int(soup.find('span', {'class': 'view-count'}).text.split()[0].replace(',', ''))
# string_date = soup.find('div', {'id': 'info-strings'}).text
#
# date_date = datetime.datetime.strptime(string_date, '%b %d, %Y')
# string_date2 = date_date.strftime('%Y-%m-%d')
#
# print(video_views)
# print(string_date)
# print(string_date2)
