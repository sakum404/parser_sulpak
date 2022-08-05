import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd


url = 'https://www.sulpak.kz/f/noutbuki/atyrau'
data = []
r = requests.get(url)
result = r.content
soup = BeautifulSoup(result, 'lxml')
pagination = soup.find('div', class_='pagination').find_all('a')
pages = pagination[-2].text
print('Всего страниц: ' + pages)
cards = soup.find_all('li', class_='tile-container')

for page in range(1, int(pages) + 1):
    r = requests.get(url, params={page: 2})
    result = r.content
    soup = BeautifulSoup(result, 'lxml')
    print(f'Парсинг страницы {page} из {pages}...')

    for card in cards:
         data.append({
             'Брэнд' : card.get('data-brand'),
             'Название' : card.get('data-name'),
             'Цена' : card.get('data-price'),
             'Ссылка' : 'https://www.sulpak.kz' + card.find('a').get('href'),
             'Артикул' : card.get('data-code')
         })

for d in data:
    print(d)
print('Всего позиций: ' + str(len(data)))

exl = pd.DataFrame(data)
exl.to_excel('suplak.xlsx')



