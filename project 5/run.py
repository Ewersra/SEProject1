#Rylie Ewers, Decker Gramlich
#cs325 project 5


from module_1.getsite import getSite
from module_2.getdata import getHTML
from module_3.getcomments import getCleanData
from module_4.getSentiments import getSentiments


#creates a list of urls from text file
file = open("data/urls.txt", "r")
text = file.read()
file.close()
urls = text.split('\n\n')

for i in range(0, 1):

    #sends the url to getsite, which requests the website
    website = getSite(urls[i])

    #sends the website data to getdata, which grabs the html from the page
    data = getHTML(website, "data/raw/output" + str(i + 1) + ".txt")

    #sends the page html to getcomments, which grabs the comments from the html, returns a file of comments
    comments = getCleanData(data, "data/processed/comments" + str(i + 1) + ".txt")

    #sends the comments to project4, which sends a prompt with the comments to ChatGPT to get the sentiments, returns a file of sentiments
    sentiments = getSentiments(comments, "data/sentiments/sentiments" + str(i + 1) + ".txt")