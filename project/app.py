from flask import Flask, render_template
from models.item import items

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/item')
# def item():
#     items = {
#         "name": ,
#         "price": ,
#         "rented": ,
#     }
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/delete/<item_id>')
def delete(item_id):
    items.objects(id = item.id).delete()
@app.route('/info/<item_id>')
def info(item_id):
    items.objects.get(id = item_id)
    return render_template('item.html')
if __name__ == '__main__':
  app.run(debug=True)
