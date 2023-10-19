import sys
import requests

def getSite(url):
    website = requests.get(url)