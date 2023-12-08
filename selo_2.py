import undetected_chromedriver
import time
from selenium import webdriver
import json


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_expermental_option('excludeSwitches', ['enable-automation'])
#options.add_experimental_option('useAutomationExtension', False)

driver = undetected_chromedriver.Chrome(options=options)


TOPICS = ['obshhestvoznanie']

def parse_page_source(source_text):
    # list [ url ]
    pass

LINKS = []
for topic in TOPICS:
    for page in range(1, 300):
        url = f'https://schoolotvety.ru/category/{topic}/page/{page}'
        driver.get('https://schoolotvety.ru/category/obshhestvoznanie/')
        time.sleep(10)
        outputs = parse_page_source(driver.page_source)

        LINKS += outputs
        with open('output.json', 'w') as f:
            f.write('\n'.join(LINKS))


# try:
print('here')
driver.get('https://schoolotvety.ru/category/obshhestvoznanie/')
time.sleep(15)
print('here3')
print(driver.page_source)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

