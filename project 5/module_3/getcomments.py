#Rylie Ewers, Decker Gramlich
#cs325 project 5

from bs4 import BeautifulSoup
import os.path

def getCleanData(data, outfile):

    outputFile = open(outfile, 'w')

    soup = BeautifulSoup(data, 'html.parser')
    #  comments = soup.find(id="thing_t1_k14hbrh").get_text()

    comments = soup.get_text()
    print(comments, file = outputFile)

    print(comments, file = outputFile)
    outputFile.close()