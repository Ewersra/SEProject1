#Rylie Ewers, Decker Gramlich
#cs325 project 5

from bs4 import BeautifulSoup
import os.path

def getComments(data, outfile):

    outputFile = open(outfile, 'w', encoding='utf-8')

    #parse html with soup
    soup = BeautifulSoup(data, 'html.parser')

    #find comment space using the html tages
    comments = soup.find('div', {'class': 'commentarea'})
    
    #find comments using tags
    comment_content = comments.find_all('div', {'class': 'comment'})

    x = []

    #print comments and strip white space, add a newline after comments
    for comment in comment_content:
        comment_text = comment.find('div', {'class': 'md'}).text.strip()
        print(comment_text + '\n', file = outputFile)
        x.append(comment_text)
    
    outputFile.close()

    return x
