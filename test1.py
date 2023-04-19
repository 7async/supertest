import time
import logging
import asyncio
import undetected_chromedriver as uc

from lxml import html
from collections import defaultdict
from pprint import pp
from undetected_chromedriver.webelement import By


logging.basicConfig(level=logging.INFO)


def _extract(text: str) -> defaultdict:
    tree = html.fromstring(text)
    d = defaultdict(lambda: (1, 1))

    for i in range(1, 1000):

        game_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[1]/div/p')
        date_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[1]/p[2]')

        if not game_list:
            break

        game = game_list[0].text.lower()
        date = date_list[0].text if date_list else ''

        if ('dota' not in game):
            continue

        if date and 'Live' in date:
            continue

        team1_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[1]/div[1]/p')
        team2_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[1]/div[3]/p')
        fact1_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[2]/div/div[1]/button/span[2]')
        fact2_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[2]/div[2]/div/div[2]/button/span[2]')

        team1 = team1_list[0].text if team1_list else None
        team2 = team2_list[0].text if team1_list else None
        fact1 = fact1_list[0].text if fact1_list else 1
        fact2 = fact2_list[0].text if fact2_list else 1

        teams = (team1, team2)
        facts = (fact1, fact2)

        d[teams] = facts
    return d

# 'https://betboom.ru/esport'

async def extract():

    url = 'https://www.ligastavok.ru/cybersport/all'

    start = time.perf_counter()

    logging.info('Starting...')

    options = uc.ChromeOptions()
    options.add_argument('--headless')

    driver = uc.Chrome(options=options)
    driver.implicitly_wait(10)

    end = time.perf_counter()
    print(end - start)
    start = time.perf_counter()

    logging.info('Getting page...')
    driver.get(url)

    logging.info('Page is loaded')
    logging.info('Waiting 15 seconds...')
    await asyncio.sleep(15)

    if len(driver.page_source) < 100000:
        await asyncio.sleep(5)

    page = driver.page_source
    d = _extract(page)
    logging.info('Closing driver...')
    driver.quit()
    logging.info('Driver closed')

    end = time.perf_counter()

    print(end - start)

    return d