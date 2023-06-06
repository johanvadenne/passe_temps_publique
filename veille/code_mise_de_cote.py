from bs4 import BeautifulSoup
import pprint
import pyperclip




fichier = open("test.txt", "r+", encoding="utf-8")
test = fichier.read()
fichier.close()

soup = BeautifulSoup(test, 'html.parser')

href = soup.find_all('a')
text = ""
for i in href:
    print('"'+str(i.get('href'))+'"')
    text += '"'+str(i.get('href'))+'",\n'

pyperclip.copy(text)