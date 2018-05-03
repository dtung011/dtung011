#1 download website
from urllib.request import urlopen

url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode('utf8')

# itunes_file = open('itunes.html', 'wb')
# itunes_file.write(raw_data)
# itunes_file.close()

from bs4 import BeautifulSoup
import pyexcel
soup = BeautifulSoup(text, 'html.parser')
section = soup.find("section", 'section chart-grid')

li_list = section.find_all("li")
item_list = []
for li in li_list:
    a1 = li.h3.a
    a2 = li.h4.a
    title = a1.string
    artist = a2.string
    link = url + a1['href']
    item = {"Title": title, "Link": link, "Artist": artist}
    item_list.append(item)
print (item_list)
pyexcel.save_as (records = item_list, dest_file_name = "itunes.xlsx")

from youtube_dl import YoutubeDL
options = {'default_search': 'ytsearch', 'max_downloads': 1}
dl = YoutubeDL(options)
for i in item_list:
    dl.download (i["Title"])