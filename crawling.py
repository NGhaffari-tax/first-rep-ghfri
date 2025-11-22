import requests
import http
import BeautifulSoup
'''from bs4 import BeautifulSoup'''

url= 'https://fantasytoys.ir'

req = requests.get(url)

if req.status_code == 200:

    print("Page fetched successfully!")
    print (req.url)
    print (req.request)

else:
    print("Failed to fetch the page.")

   
soup = BeautifulSoup(req.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")