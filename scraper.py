import csv
import requests
import re
from bs4 import BeautifulSoup


ORIGINALS = []


def scrape(url, stop):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    for pos in soup.find_all('i'):
        a = re.sub('<a .*">', '', str(pos))
        a = a.replace('</a>', '')
        a = a.split('i>')[1].split('</')[0]
        if a == stop:
            break
        ORIGINALS.append([a])


if __name__ == '__main__':
    dummy = 'dummy for movies'
    urls = [
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_programming', 'Skam Italia'),
        ('https://en.wikipedia.org/wiki/List_of_ended_Netflix_original_programming', 'Arrested Development'),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2015–2017)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2018)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2019)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2020)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2021)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2022)', dummy),
        ('https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2023)', 'Heart of the Hunter')
    ]
    for pair in urls:
        scrape(pair[0], pair[1])

    with open('./originals.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title'])
        writer.writerows(ORIGINALS)