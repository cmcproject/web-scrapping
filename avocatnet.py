# --- Web Scraping with BeautifulSoup ---
import requests
from bs4 import BeautifulSoup
import pandas as pd

PAGES = 10

all_questions = []
for page in range(0, PAGES):
    response = requests.get(f"https://www.avocatnet.ro/forum*{page}")
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.find_all('div', {'class': 'listing-forum listing-extins m-action-parent'})
    all_questions.append(questions)

# print(type(questions[0]))
# print(questions[0].get("id", 0))

master_list = []
for questions in all_questions:
    for question in questions:
        info = question.find_all('span', {'class': 'celula'})[1]
        titlu = info.find_all('a')[2].text.strip()
        print(f'Titlu: {titlu}')
        link = info.find('h5').find('a')['href']
        print(f'Link: https://www.avocatnet.ro{link}')

        mesaje = question.find_all('span', {'class': 'cifre'})[0].text
        print('Mesaje: ', mesaje)

        vizualizari = question.find_all('span', {'class': 'cifre'})[1].text
        print('Vizualizari: ', vizualizari)

        data = question.find('span', {'class': 'afiseaza-data'}).text
        print('Data: ' + data)

        categorie = info.find('span', {'class': 'hide-mobile'}).find('a').text
        print('Categorie: ' + categorie)

        data_dict = {'titlu': titlu,
                     'data': data,
                     'categorie': categorie,
                     'link': f'https://www.avocatnet.ro{link}',
                     'mesaje': mesaje,
                     'vizualizari': vizualizari}
        master_list.append(data_dict)

print(f'Intrari: {len(master_list)}')
avocatnet_df = pd.DataFrame(master_list)
avocatnet_df.to_csv('avocatnet.csv')
