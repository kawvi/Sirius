import undetected_chromedriver
import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_expermental_option('excludeSwitches', ['enable-automation'])
#options.add_experimental_option('useAutomationExtension', False)

driver = undetected_chromedriver.Chrome(options=options)


TOPICS = ['obshhestvoznanie']

def parse_page_source(source_text):
    # list [ url ]
    soup = BeautifulSoup(source_text, 'html.parser')
    divs = soup.find_all('header', class_='entry-header')
    links = []
    for div in divs:
        project_url = div.find('div', class_='entry-title').find('a').get('href')
        links.append(project_url)
    return links



def wait_until_captcha_is_done(driver):
    max_retries = 20
    
    while max_retries != 0:
        time.sleep(3)
        print('DRIVER: ', driver)
        links = parse_page_source(driver.page_source)
        if links:
            return links
    
        max_retries -= 1

    return []

    

LINKS = []
for topic in TOPICS:
    for page in range(1, 60):
        url = f'https://schoolotvety.ru/category/{topic}/page/{page}'
        print(url)
        driver.get(url)


        outputs = wait_until_captcha_is_done(driver)
        
        print('New items: ', len(outputs))
        
        LINKS += outputs
        with open('output.json', 'w') as f:
            f.write('\n'.join(LINKS))


# driver.close()


# driver.quit()
