from gmail import GMail, Message
from random import choice
from datetime import datetime
n = datetime.now()

x = "tunghr.des@gmail.com"

html_template = "<p>em ch&agrave;o sếp, em bị {{bịnh}}, sếp cho em nghỉ nh&eacute; hihi</p>"

sickness_list = ["Thương hàn", "ỉa chảy", "AIDS"]

html_content = html_template.replace("{{bịnh}}", choice(sickness_list))

gmail = GMail('gottenvn@gmail.com','Tung11112010')
msg = Message("Tung smile", to = x, html = html_content)

if n.hour > 7:
    gmail.send(msg)