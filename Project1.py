import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
#print(URL)

website = requests.get(url)

soup = BeautifulSoup(website.content, 'html5lib')


outputFile = open('output.txt', 'w')
print(soup.prettify(), file = outputFile)
outputFile.close()
