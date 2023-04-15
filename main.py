import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


try:
    options = uc.ChromeOptions()
    options.add_argument('--headless')

    driver= uc.Chrome(options=options)
    driver.implicitly_wait(13)

    url = 'https://www.ligastavok.ru/cybersport/dota-2'

    driver.get(url)


    elements = []
    for i in range(1, 30):

        try:    
            team1 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[1]/div[1]/p')
            team2 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[1]/div[3]/p')

            fact1 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[2]/div/div[1]/button/span[2]')
            fact2 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[2]/div/div[2]/button/span[2]')
                
            print(team1.get_attribute('innerHTML'), team2.get_attribute('innerHTML'))
            print(fact1.get_attribute('innerHTML'), fact2.get_attribute('innerHTML'))
        except:
            print('skipped')
except:
    print(123)

#/html/body/div[1]/div[2]/div[2]/div/div[1]/div/ul/li[1]/div/div[2]
#/html/body/div[1]/div[2]/div[2]/div/div[1]/div/ul/li[2]/div/div[2]
#/html/body/div[1]/div[2]/div[2]/div/div[1]/div/ul/li[3]/div/div[2]
