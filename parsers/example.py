from pipeline.deco import beforeafter


def before_get_total_records(html):
    return html

def after_get_total_records(result):
    return result


def get_total_records(html):

    if len(html) > 100:
        return 3
    else:
        return False

def before_get_links(html):
    return html

def after_get_links(result):
    return result



def get_links(html):

    if len(html) > 100:

        return [
            'http://localhost:8000/product/1',
            'http://localhost:8000/product/2',
            'http://localhost:8000/product/3',
        ]


def before_get_metadata(html):
    return html

def after_get_metadata(result):
    return result

def get_metadata(html):

    if len(html) > 100:

        return ['http://localhost:8000/product_list']


