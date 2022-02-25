# --- Web Scraping with BeautifulSoup ---
import requests
from bs4 import BeautifulSoup

PAGES = 10

all_questions = []
for page in range(1, PAGES):
    response = requests.get(f"https://stackoverflow.com/questions?tab=unanswered&page={page}")
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.find_all('div', {'class': 'question-summary'})
    all_questions.append(questions)

# print(type(questions[0]))
# print(questions[0].get("id", 0))

for questions in all_questions:
    for question in questions:
        print(question.find('a', {'class': 'question-hyperlink'}).text)
        print(question.find('span', {'class': 'vote-count-post'}).text)
