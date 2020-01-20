import requests
from bs4 import BeautifulSoup as soup

def getEclipseText():
    '''small function to scrape the eclipse data from a website'''

    #scrape the text on eclipses from this website
    url = 'http://metservice.intnet.mu/sun-moon-and-tides-info-eclipses.php'

    #open the connection, grab the page
    r = requests.get(url)

    #html parsing
    page_soup = soup(r.content, "html.parser")

    #the content we want is in the 'left_content' tag, and all the rows are headed with p tags, let's get a result set list
    #with these lines
    page_container = page_soup.find("div", {"class":"left_content"}).findAll("p")

    #creating empty string to hold the data
    eclipse_text = ''

    #strip the first and last line, since they aren't to do with eclipses
    page_container = page_container[1:-1]

    #grab the text from each line, and append it line-by-line to the result container
    for line in page_container:
        eclipse_text += line.text + '\n'