#1 Download Website
#2 Identify ROI - Region of Interest
#3 Extract information from ROI + Process info to right format
from urllib.request import urlopen

url = "http://dantri.com.vn"
#1.1 Open connection
conn = urlopen("http://dantri.com.vn")
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
text = raw_data.decode("utf8")
# print (text)
# utf8 stands for unicode

# dan_tri_file = open("dantri.html", "wb")
# #wb stands for write binary
# dan_tri_file.write(raw_data)
# dan_tri_file.close()

#2 Find Raw
from bs4 import BeautifulSoup
import pyexcel
soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())

li_list = ul.find_all("li")
item_list = []
# print (li_list)
for li in li_list:
    a = li.h4.a
    # print (a.prettify())
    title = a.string # take string or content
    # print (title)
    link = url + a["href"]
    item = {
        "Title": title,
        "Link": link
    }
    item_list.append(item)
print (item_list)
pyexcel.save_as (records = item_list, dest_file_name = "dantri.xlsx")