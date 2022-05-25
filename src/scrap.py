import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://nofluffjobs.com/pl/praca-zdalna'
webpage = requests.get(url)
bs = BeautifulSoup(webpage.content, 'html.parser')

title = [title.text for title in bs.find_all(class_='posting-title__position')]
company = [company.text for company in bs.find_all(class_='posting-title__company')]
link = [link['href'] for link in bs.find_all(class_='posting-list-item')]

jobs = pd.DataFrame(
    {'title': title,
     'company': company,
     'link': link,
     'source': 'nfj'
     })

print(jobs.to_string())
