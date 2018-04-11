import requests
from bs4 import BeautifulSoup 
import json
import pandas as pd

# get amazon reviews after 1/1/2017 and store as json file

url = 'https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_arp_d_viewopt_srt?sortBy=recent&pageNumber='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_reviews = pd.DataFrame(columns = ['name','date','content'])

for x in xrange(1,100):
    print x
    html = requests.get(url + str(x), headers = headers).content
    soup = BeautifulSoup(html,'html.parser')
    comment_list_soup = soup.find('div', attrs={'id': 'cm_cr-review_list'})

    for comment_soup in comment_list_soup.find_all('div',attrs={'data-hook':'review'}):
        if comment_soup:
            name = comment_soup.find('a', attrs = {'data-hook' : 'review-author'}).getText()
            date = comment_soup.find('span', attrs = {'data-hook' : 'review-date'}).getText()[3:]
            #if year is less than 2017 
            if date[-4:] < "2017":
                break
            content = comment_soup.find('span', attrs = {'data-hook' : 'review-body'}).getText()
            review_data = [name,date,content]
            df_reviews.loc[len(df_reviews)] = review_data
    else:
        continue
    break

output = df_reviews.to_json(orient='records')
with open('reviews.json', 'w') as f:
    f.write(output)
