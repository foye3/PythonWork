import requests
from bs4 import BeautifulSoup
import codecs

# get hottest comments of Ready Player One on douban.com

download_url = 'https://movie.douban.com/subject/4920389/comments'
url_param = '?sort=new_score&status=P'
#'?start=220&limit=20&sort=new_score&status=P&percent_type='

def download_page(url):
    # minght refuse response because request recognized sent by a spider program.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Cookie' : '',
        'Connection' : 'keep-alive'
    }
    data = requests.get(url,headers = headers).content
    return data



def parse_html(html):
    #create a BeautifulSoup object
    soup = BeautifulSoup(html,'html.parser')
    
    comment_list_soup = soup.find('div', attrs={'class': 'mod-bd'})

    comment_list = []
    for comment_li in comment_list_soup.find_all('div'):
        detail = comment_li.find('div', attrs={'class': 'comment'})
        if detail:
            comment_info = detail.find('h3').find('span',attrs={'class':'comment-info'})
            user_name = comment_info.find('a').getText()
            #print user_name
            user_link = comment_info.find('a')['href']
            #print user_link
            rating_span = comment_info.find('span',attrs={'class':'rating'})
            rating = ''
            if rating_span:
                rating = rating_span['class'][0]
                rating = rating[-2:]
            #print rating
            comment_list.append(user_name + ' ' + rating + ' ' + user_link)
            comment = detail.find('p').getText().rstrip()
            comment_list.append(comment)
            comment_list.append(' ')
            #print comment   
    next_page = soup.find('a',attrs={'class':'next'})
    if next_page:
        print next_page['href']
        return comment_list, download_url + next_page['href']
    return comment_list, None


def main():
    url = download_url + url_param
    html = download_page(url)
    parse_html(html)
    with codecs.open('ReadyPlayerOneComments', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            comments, url = parse_html(html)
            fp.write(u'{comments}\n'.format(comments='\n'.join(comments)))

if __name__ == '__main__':
    main()