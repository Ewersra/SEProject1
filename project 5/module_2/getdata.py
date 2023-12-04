#Rylie Ewers, Decker Gramlich
#cs325 project 5

from bs4 import BeautifulSoup

def getHTML(website, outfile):
    #parse the html file with beaitiful soup
    soup = BeautifulSoup(website.content, 'html.parser')
    #open output file
    outputFile = open(outfile, 'w', encoding='utf-8')
    print(soup, file = outputFile)
    outputFile.close()
    return soup.prettify()
