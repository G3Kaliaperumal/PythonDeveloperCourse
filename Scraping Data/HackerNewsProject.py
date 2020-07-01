import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hacker_news(links, votes):
  hn = []
  for index, link in enumerate(links):
    points = int(votes[index].getText().replace(' points', ''))
    print(points)
    if points > 150:
      title = link.getText()
      href = link.get('href', None)
      hn.append({'title': title, 'link': href})
  return hn
    
print(create_custom_hacker_news(links, votes))
