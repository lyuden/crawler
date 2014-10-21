from flask import  Flask

app = Flask(__name__)

PRODUCT_TEMPLATE = """
<html>
    <head></head>
    <body>
         <div id = "product">
            <div id = "id">
               id{}
            </div>
            <div id = "title">
               title{}
            </div>
            <div id = "description">
               decscription{}
            </div>
         </div>
    </body>
</html>

"""

CATALOG_TEMPLATE = '''
<html>
    <head></head>
    <body>
         <div id = "products">
            {}
         </div>
         <div id = "page">
         Page {} of 10
         </div>
    </body>
</html>
'''


@app.route('/products/<int:id>/')
def product_route(id):
    return PRODUCT_TEMPLATE.format(id, id, id)

@app.route('/catalog/<int:page>/')
def product_list(page):

    return CATALOG_TEMPLATE.format("\n".join('''
    <div class="product_link">
        <a href="/products/{}">Product{} </a>
    </div>'''.format(i, i) for i in range(10*page, 10*page + 7)),
                                   10
    )








if __name__ == "__main__":

    app.run(debug=True)