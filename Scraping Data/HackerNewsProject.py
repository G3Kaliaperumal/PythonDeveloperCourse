import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_points(hn_list):
  return sorted(hn_list, key = lambda k:k['points'], reverse = True)

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
  return sort_stories_by_points(hn)
    
pprint(create_custom_hacker_news(mega_links, mega_subtext))