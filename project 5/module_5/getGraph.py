#Rylie Ewers, Decker Gramlich
#cs325 project 6

import pandas as pd
import matplotlib.pyplot as plt

def getGraph(list, url, outpath):
    
    #sanitizing the url to use as the plot header
    url1 = url.split('/') #spliting the url by '/'
    url2 = url1[-2] #taking the last part of the path, which is the title of the post. the list has a blank string at the end which is why the its [-2]
    url3 = url2.replace('_', ' ') #replacing the underscores with spaces
    url4 = url3.capitalize() #capitalizing the first letter
    
    #creating the series to be used for the graph
    series = pd.Series(list)
    counts = series.value_counts() #counts each occurance of a sentiment
    sorted = counts.sort_index() #sorts the in alphabetical order
    
    colors = ['blue', 'red', 'green', 'yellow', 'hotpink', 'cyan', 'orange', 'purple', 'brown', 'black'] #colors for the bars in the graph

    plt.figure()

    x = plt.bar(sorted.index, sorted.values, color = colors, label = sorted.index) #creates the plot
    plt.title(url4) #uses the sanitized url as the title
    plt.xlabel('Sentiments') #creates the bottom label for the plot
    plt.legend(x, [f'{index}' for index in sorted.index], loc='upper right') #creates the legend
    plt.savefig(outpath) #saves it
