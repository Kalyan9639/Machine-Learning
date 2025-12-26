'''
Real-World Use case: Web Scraping using Multi-Threading
'''

import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time

urls = [
    "https://mangafire.to/home",
    "https://mangafire.to/manga/saikyou-onmyouji-no-isekai-tenseiki-geboku-no-youkaidomo-ni-kurabete-monster-ga-yowaisugirundagaa.vv05v",
    "https://mangafire.to/filter?keyword=isekai&vrf=5fcaUfZo7rW1-Z3vTEvXO5sJBfP2eeTM2NIVmftLuGhYVi8cHYn2wA"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} chars from {url}")

# current = time.time()
# with ThreadPoolExecutor(max_workers=30) as executor:
#     results = executor.map(fetch_content,urls)
# final = time.time() - current

threads = []
current = time.time()
for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

final = time.time() - current

print(f"All web pages fetched in {final} sec")
