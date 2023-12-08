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


with open('url_obshestvoznanie.txt') as f:
    LINKS = f.read().split()[:10]

def parse_page(source_text):
    soup = BeautifulSoup(source_text, 'html.parser')
    content_div = soup.find('div', class_='entry-content')

    if not content_div:
        return None

    text = "\n".join(el.text for el in content_div)
    question, answer = text.split("Ответ")

    return {"query": question.strip(), "answer": answer.strip()}


def wait_until_captcha_is_done(driver):
    max_retries = 20
    
    while max_retries != 0:
        time.sleep(3)
        output = parse_page(driver.page_source)
        if output:
            return output
    
        max_retries -= 1

    return None


# {"question": "...", "answer": "...", "explanation": "..."}

OUTPUT = [] 
for link in LINKS:
    print(link)
    driver.get(link)

    OUTPUT.append(wait_until_captcha_is_done(driver))

    with open('output_final_obshestvo.json', 'w') as f:
        f.write(json.dumps(OUTPUT))
    
    print('Total size: ', len(OUTPUT))
        
