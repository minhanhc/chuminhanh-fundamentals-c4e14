from flask import Flask, render_template, request, redirect, url_for, flash
from models.item import items

from mlab import mlab_connect
app = Flask(__name__)
app.config["SECRET_KEY"] = "chuminhanh"
mlab_connect()

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
    return render_template('admin.html', items = items.objects)
@app.route('/delete/<item_id>')
def delete(item_id):
    items.objects(id = item_id).delete()
    return redirect(url_for('admin'))

@app.route('/info/<item_id>')
def info(item_id):
    items.objects.get(id = item_id)
    return render_template('item.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        new_item = items(name = name, duration = 0, rented = False )
        new_item.save()
        flash("Đã đăng kí thành công")
        return redirect(url_for('form'))
@app.route('/edit/<item_id>')
def edit(item_id):
    item = items.objects().with_id(item_id)
    if item is None:
        return "Not found"
    else:
        return render_template('edit.html', item = item)
@app.route('/update')
def update():
    renteds = items.objects(duration__gt = 0)
    for rented in renteds:
        if rented.rented is False:
            rented.update(set__rented = True)
    return redirect(url_for('admin'))
if __name__ == '__main__':
  app.run(debug=True)
