import requests
from bs4 import BeautifulSoup
import re

website = "https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0" 
cookies = "session-id=134-5506682-5036729; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=134-6425206-0770933; session-token=nR3g7w7tFhcIpnuLO2PpnFNZH7wkzzVlMOJ7a8y+9oFNa1zofjf7izsN8E2oDdymLNRCFkOLd7Ug11ycTbOOXk+GUnD9/GV/1FKBZzQ3gTcCLq86dllpByVoXn70TNlnURIixnNi2WfaVFDO+i+WemOWP71t0c7PM9gwWCYhEX8rrkMS7KW2jje8ch9ke5CY; csm-hit=tb:s-28WDK67AWKST937J8WH5|1638663128778&t:1638663134504&adb:adblk_no"

headers = {"User-Agent": user_agent, "Cookie": cookies}
s = requests.session()

html = s.get(website, headers=headers)
soup = BeautifulSoup(html.text, "html.parser")
price = soup.find(id="attach-base-product-price")
title = soup.find(id="productTitle").get_text().strip()

print (title)
print ("Precio: $" + price["value"])
