import urllib3
from lxml import html
from bs4 import BeautifulSoup

BASE_URL = "https://scholar.google.com/citations?user=i9jzs1oAAAAJ&hl=en&oi=ao"

http = urllib3.PoolManager()

response = http.request("GET", BASE_URL).data

html_str = str(response).replace("b'<!doctype html>", "")

test_html = """
<html>
  <head><title>The Title</title></head>
  <body>
    <p class="title"><b>The Bold Title</b></p>
    <p class="title"><b>The Bold Title</b></p>
    <p class="title"><b>The Bold Title</b></p>
    <p class="story">The Bold Title</p>
    <p class="story">Once upon a time...</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
table_rows = soup.find_all(class_="gsc_a_tr") #gsc_a_tr

titles = soup.find_all(class_="gsc_a_at")

print(titles[0])
