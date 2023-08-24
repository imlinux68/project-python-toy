#pip install

from urllib.request import urlopen

page=urlopen("https://ynet.co.il")
print(page.headers)
