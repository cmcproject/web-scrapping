# --- Web Scraping with BeautifulSoup ---
import requests
from bs4 import BeautifulSoup

PAGES = 10

all_questions = []
for page in range(1, PAGES):
    response = requests.get(f"https://stackoverflow.com/questions?tab=unanswered&page={page}")
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".question-summary")
    all_questions.append(questions)


# print(type(questions[0]))
# print(questions[0].get("id", 0))

for questions in all_questions:
    for question in questions:
        print(question.select_one(".question-hyperlink").getText())
        print(question.select_one(".vote-count-post").getText())

