#Rylie Ewers, Decker Gramlich
#cs325 project 5

import requests

def getSite(url):
    website = requests.get(url)
    return website