#Rylie Ewers, Decker Gramlich
#cs325 project 5

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

def getSite(url, headers):
    website = requests.get(url, headers=headers)
    return website
