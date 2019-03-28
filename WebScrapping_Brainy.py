from bs4 import BeautifulSoup
from requests import get
from time import sleep
from random import randint

def scrapedata(url, noofpages = 1):
    if noofpages == 1: # scrape 1 page only. Any other number, scrape authors from a - z.
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
# write data to file. Syntax is for Mac OS;
        with open('~\.authorslist.txt','w') as output:
            
# authors_container = html.soup.find_all('div', class_ = 'row bq_left')
            for span in html_soup.find('div', class_='row bq_left').findAll('span'):
                output.write(span.text + '\n')
        output.close()
        print ("Results saved in '~\.authorslist.txt'")

    else: # scrape multiple pages
        for i in range(97, 123): # iterating alphabet a - z using ascii codes
            if i > 98: # Break out of the loop to skip authors starting with letter c to save time.
                break
            for j in range(1,21): # iterating 20 sub pages of an alphabet
                url_ = ''
                if j == 1:
                    url_ = url + '/' + chr(i)
                else:
                    url_ = url + '/' + chr(i) + str(j)
                try:
                    response = get (url_)
                    html_soup = BeautifulSoup(response.text, 'html.parser')
# write data to file. Syntax is for Mac OS;
                    with open('~\.authorslist' + chr(i).upper() + '.txt','w+') as output:
            
# authors_container = html.soup.find_all('div', class_ = 'row bq_left')
                        for span in html_soup.find('table', class_='table table-hover table-bordered').findAll('a'):
                            output.write(span.text + '\n')
                    output.close()
                    sleep(randint(1,4)) # randomly rest between 1 - 3 seconds
                except:
                    break
            print ("Results saved in '~\.authorslist" + chr(i).upper() + ".txt'")


# Change the 2nd parameter to > 1 when calling scrapedata function to scrape multiple pages.
# ------------------------------------------------------
### scrapedata('https://www.brainyquote.com/authors', 1)
# ------------------------------------------------------

# For eg, use the below to scrape all authors from a - z.
# ------------------------------------------------------
scrapedata('https://www.brainyquote.com/authors', 2)
# ------------------------------------------------------
