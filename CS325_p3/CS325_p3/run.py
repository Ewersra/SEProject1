import sys
#import os.path
import module_1
from getsite import getSite
sys.path.insert(0, '\CS325_p3\module_1')
#from getdata import getHTML
#from getcomments import getCleanData

url = sys.argv[1]

website = getsite.getSite(url)

data = getdata.getHTML(website)

comments = getcomments.getCleanData(data)