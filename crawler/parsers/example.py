from bs4 import BeautifulSoup
import re


def get_total_records(html):

    try:
        soup = BeautifulSoup(html)

        pagetext = soup.select("div#page").text
        t = soup.select("div#page")[0].text.strip()
        pagestr = re.match('Page \d+ of (?P<limit>\d+)',t).groupdict()['limit']
        return int(pagestr)

    except:

        return False



def get_links(html):

    soup = BeautifulSoup(html)

    return ['http://localhost:5000{}'.format(a.attrs['href']) for a in soup.find_all('a')]

def get_metadata(html):


    soup = BeautifulSoup(html)
    prdiv = soup.select('div#product')[0]

    id = prdiv.select('div#id')[0].text.strip()
    title = prdiv.select('div#title')[0].text.strip()
    description = prdiv.select('div#description')[0].text.strip()

    return {'id':id,
            'title':title,
            'description': description
            }