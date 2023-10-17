from bs4 import BeautifulSoup
import os.path

def getCleanData(data):
    os.chdir("Data")
    os.chdir("raw")
    file = 'output.txt'
    os.chdir("Data")
    os.chdir("processed")
    f = open(file, errors="ignore")
    content = f.read()
    f.close()
    outputFile = open('comments.txt', 'w', errors="ignore")

    soup = BeautifulSoup(content, 'html.parser')
    #  comments = soup.find(id="thing_t1_k14hbrh").get_text()

    comments = soup.get_text()
    print(comments, file = outputFile)

    print(comments, file = outputFile)
    outputFile.close()
    