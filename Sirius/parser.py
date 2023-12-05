from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/tutor/subject/?subject_id=10'
page = requests.get(url)
page.encoding = 'utf-8'

soup = BeautifulSoup(page.text, 'html.parser')

projects_urls = []
divs = soup.find_all('div', class_='Text Text_size_m TopicListCard-LinkText TopicListCard-LinkText_spaced')
for div in divs:
    project_url = 'https://yandex.ru' + div.find('a').get('href')
    projects_urls.append(project_url)

for project_url in projects_urls:
    req = requests.get(project_url)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')

    projects_datas = soup.find_all('div', class_='Task-Description')

    for project_data in projects_datas:
        print(project_data.text)

