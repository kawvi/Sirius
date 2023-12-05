from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=274&tag_id=19'
request = requests.get(url)
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')

films = soup.find_all('div', class_='Task-Description')
for film in films:
    print(film.text)


# req = requests.get(project_url)
#     soup = BeautifulSoup(req.text, 'html.parser')

#     projects_datas = soup.find_all('div', class_='Task-Description')

#     for project_data in projects_datas:
#         print(project_data.text)


# projects_datas = soup.find_all('div', class_='Task-Description')
# for project_data in projects_datas:
#     print(project_data.text)

#divs = soup.find_all('div', class_='Text Text_size_m TopicListCard-LinkText TopicListCard-LinkText_spaced')