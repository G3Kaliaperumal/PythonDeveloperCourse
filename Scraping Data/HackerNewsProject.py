import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hacker_news(links, subtext):
  hn = []
  for index, link in enumerate(links):
      title = link.getText()
      href = link.get('href', None)
      vote = subtext[index].select('.score')
      if len(vote):
        points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
          hn.append({'title': title, 'link': href, 'points': points})
  return hn
    
pprint(create_custom_hacker_news(links, subtext))
