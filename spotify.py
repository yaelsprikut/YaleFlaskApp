import requests
import json
import re
from bs4 import BeautifulSoup

page = requests.get("https://open.spotify.com/track/1fOkmYW3ZFkkjIdOZSf596?si=-8fZvB7HRuSTw_Moftl8ug")
apple_page = requests.get("https://itunes.apple.com/ca/album/sour/899380254?i=899380279")
soup = BeautifulSoup(page.content, 'html.parser')

apple_soup = BeautifulSoup(apple_page.content, 'html.parser')

pattern = re.compile(r"Spotify.Entity\s+=\s+(\{.*?\});\n")
script = soup.find("script", text=pattern)

data = pattern.search(script.text).group(1)
data = json.loads(data)
print('The artist name is: '+ data['artists'][0]['name'])
print('The song name is: '+ data['name'])

print('----------------------------------------------------')
print(apple_soup.find('title').get_text())
print(soup.find('title').get_text())

# containers = soup.find_all("script")

# print(containers.prettify())
#print(list(soup.children))
# json_response = soup.find_all('script')[4].get_text()
# print(json_response)