import requests
from bs4 import BeautifulSoup

def get_data(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    projects_urls = []
    divs = soup.find_all('div', class_='Text Text_size_m TopicListCard-LinkText TopicListCard-LinkText_spaced')
    for div in divs:
        project_url = 'https://yandex.ru' + div.find('a').get('href')
        projects_urls.append(project_url)
    
    for project_url in projects_urls:
        req = requests.get(project_url)
        req.encoding = 'utf-8'

        soup = BeautifulSoup(req.text, 'html.parser')
        questions = soup.find_all('div', class_='Task-Description')
        for question in questions:
            print(question.text)
        '''парсинг вопросов'''


        # soup = BeautifulSoup(req.text, 'html.parser')
        # explanations = soup.find_all('div', class_='Text Text_size_m TaskBlock TaskBlock_type_text TaskBlock_parentBlock_ResultLine')
        # for explanation in explanations:
        #     print(explanation.text)
        # '''парсинг объяснений'''
        

        # soup = BeautifulSoup(req.text, 'html.parser')
        # answers = soup.find_all('div', class_='Row Row_gapTop_m')
        # for answer in answers:
        #     print(answer.text)


        

get_data('https://yandex.ru/tutor/subject/?subject_id=10')