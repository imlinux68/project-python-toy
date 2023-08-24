#pip install google

import search from googlesearch


query="Israel travel guide"
for i in search(query,start=0,pause=2):
    print(i)
