#Rylie Ewers, Decker Gramlich
#cs325 project 6

from module_1.getSite import getSite
from module_2.getHTML import getHTML
from module_3.getComments import getComments
from module_4.getSentiments import getSentiments
from module_5.getGraph import getGraph

#creates a list of urls from text file
file = open("data/urls.txt", "r")
text = file.read()
file.close()
urls = text.split('\n\n')


key = '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'

for i in range(0, len(urls)):

    #sends the url to getSite, which requests the website
    website = getSite(urls[i])
    
    #sends the website data to getHTML, which grabs the html from the page
    data = getHTML(website, "data/raw/output" + str(i + 1) + ".txt")
    print("HTML file for url " + str(i + 1) + " is done.")

    #sends the page html to getComments, which grabs the comments from the html, returns a file of comments
    comments = getComments(data, "data/processed/comments" + str(i + 1) + ".txt")
    print("Comments file for url " + str(i + 1) + " is done.")

    #sends the comments to getSentiments, which sends a prompt with the comments to ChatGPT to get the sentiments, returns a file of sentiments
    sentiments = getSentiments(key, comments, "data/sentiments/sentiments" + str(i + 1) + ".txt")
    print("Sentiments file for url " + str(i + 1) + " is done.")

    #
    getGraph(sentiments, urls[i], "data/plots/plot" + str(i + 1) + ".png")
    print("Graph file for url " + str(i + 1) + " is done.")
