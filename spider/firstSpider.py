import requests
from bs4 import BeautifulSoup
import codecs

# get top 250 famours movies on douban.com

download_url = 'https://movie.douban.com/top250'

def download_page(url):
    # minght refuse response because request recognized sent by a spider program.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers = headers).content
    return data



def parse_html(html):
    #create a BeautifulSoup object
    soup = BeautifulSoup(html,'html.parser')
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

    movie_name_list = []
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(movie_name)
        #print movie_name
    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        print next_page
        return movie_name_list, download_url + next_page['href']
    return movie_name_list, None


def main():
    url = download_url

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()