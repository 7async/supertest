import time
import undetected_chromedriver as uc
from undetected_chromedriver.webelement import By

# 'https://betboom.ru/esport'

url = 'https://www.ligastavok.ru/cybersport/all'

driver = uc.Chrome()
driver.implicitly_wait(10)
driver.get(url)
time.sleep(10)

print(driver.page_source, file=open('page.html', 'w', encoding='utf-8'))

input('ENTER')