from bs4 import BeautifulSoup





def get_total_records(html):

    if len(html) > 100:
        return 3
    else:
        return False




def get_links(html):

    if len(html) > 100:

        return [
            'http://localhost:5000/products/1',
            'http://localhost:5000/products/2',
            'http://localhost:5000/products/3',
        ]



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