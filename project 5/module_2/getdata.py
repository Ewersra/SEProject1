#Rylie Ewers, Decker Gramlich
#cs325 project 5

from bs4 import BeautifulSoup

def getHTML(website, outfile):
    soup = BeautifulSoup(website.content, 'html.parser')
    outputFile = open(outfile, 'w', encoding='utf-8')
    print(soup.prettify(), file = outputFile)
    outputFile.close()
    return soup.prettify()
