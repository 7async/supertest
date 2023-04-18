from lxml import html
from collections import defaultdict
from pprint import pp

text = open('page.html', 'r', encoding='utf-8').read()
tree = html.fromstring(text)
d = defaultdict(lambda: (1, 1))

cnt = 0
for i in range(1, 1000):

    game_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[1]/div/p')
    date_list: list[html.HtmlElement] = tree.xpath(f'//*[@id="content"]/div[1]/div/ul/li[{i}]/div/div[1]/p[2]')

    if not game_list:
        break

    game = game_list[0].text.lower()
    date = date_list[0].text if date_list else []

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

    cnt += 1

print(cnt)
pp(d)
