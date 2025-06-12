from bs4 import BeautifulSoup
import requests

def parse():
    URL = 'https://www.olx.uz/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'inner')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_= 'link linkWithHash detailsLinkPromoted').get_text(strip=True),
           	
        })

        for comp in comps:
            print(comp["title"])
 


parse()