import sys
sys.path.insert(1, 'D:\module_1')
import getsite
import getdata
import getcomments

url = sys.argv[1]

website = getsite.getSite(url)

data = getdata.getHTML(website)

comments = getcomments.getCleanData(data)