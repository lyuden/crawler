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


@app.route('/products/<int:id>/')
def product_route(id):

    return PRODUCT_TEMPLATE.format(id,id,id)


if __name__ == "__main__":

    app.run()