tincidae - crawler without blackjack and hookers
------------
Just a teeny tiny part of [pholcidae](https://github.com/bbrodriges/pholcidae) with a bit of context magic.

Dependencies
------------
* python 3 or higher

Usage example
------------
``` python
from tincidae import crawl

with crawl('http://google.com/') as page:
	print(page['headers'], page['status'], page['cookies'], page['body'])
```