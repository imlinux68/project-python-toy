#pip install

from urllib.request import urlopen


page=urlopen("https://ynet.co.il")
sourcecode=page.read()
print(sourcecode)
