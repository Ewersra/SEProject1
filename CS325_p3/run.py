import sys
from module_1.getsite import getSite
from module_2.getdata.py import getHTML
from module_3.getcomments.py import getCleanData
from module_4.getSentiments import getSentiments

#get the reddit URL from the command line
url = sys.argv[1]

#sends the url to getsite, which requests the website
website = getsite.getSite(url)

#sends the website data to getdata, which grabs the html from the page
data = getdata.getHTML(website)

#sends the page html to getcomments, which grabs the comments from the html, returns a file of comments
comments = getcomments.getCleanData(data)

#sends the comments to project4, which sends a prompt with the comments to ChatGPT to get the sentiments, returns a file of sentiments
sentiments = getSentiments.getSentiments(comments, "data/sentiments/sentiments.txt")
