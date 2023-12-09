import undetected_chromedriver
import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from seleniumbase import Driver


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--load-extension=C:\Users\username\Desktop\extension')
#options.add_expermental_option('excludeSwitches', ['enable-automation'])
#options.add_experimental_option('useAutomationExtension', False)

#driver = undetected_chromedriver.Chrome(options=options)
driver = Driver(uc=True)


with open('sholnie_otvety.com/url_obshestvoznanie.txt') as f:
    LINKS = f.read().split()

def parse_page(source_text):
    soup = BeautifulSoup(source_text, 'html.parser')
    content_div = soup.find('div', class_='entry-content')

    if not content_div:
        return None

    answer_text, question_text = "", ""

    ans = False
    for el in content_div:
        if el.name == 'h2':
            ans = True
            continue
        if ans:
            answer_text += el.text
        else:
            question_text += el.text

    return {"question": question_text.strip(), "answer": answer_text.strip()}


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

    with open('output_final_obshestvo_1.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(OUTPUT))
    
    print('Total size: ', len(OUTPUT))
        
