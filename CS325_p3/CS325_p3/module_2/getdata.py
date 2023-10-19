from bs4 import BeautifulSoup
import os.path

def getHTML(website):
    soup = BeautifulSoup(website.content, 'html5lib')
    os.chdir("Data")
    os.chdir("raw")
    outputFile = open('output.txt', 'w')
    print(soup.prettify(), file = outputFile)
    outputFile.close()
