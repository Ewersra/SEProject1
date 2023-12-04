#Rylie Ewers, Decker Gramlich
#cs325 project 5

from bs4 import BeautifulSoup
import os.path

def getCleanData(data, outfile):

    outputFile = open(outfile, 'w')

    soup = BeautifulSoup(data, 'html.parser')

    comments = soup.find('div', {'class': 'commentarea'})

    comment_content = comments.find_all('div', {'class': 'comment'})

    for comment in comment_content:
        comment_text = comment.find('div', {'class': 'md'}).text.strip()
        print(comment_text + '\n', file = outputFile)
    
    outputFile.close()
