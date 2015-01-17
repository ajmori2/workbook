
# import the Flask class from the flask module
from flask import Flask, render_template, jsonify
from utilities import load_src

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('mainPage.html')

# Generic route for MPs
@app.route('/mp/<mpName>')
def mp(mpName):
    #load_src("mp_alice", "py/compute.py")
    load_src("mpCode", 'py/' + mpName + '/compute.py')
    from mpCode import do_compute
    do_compute()
    return render_template(mpName + '/index.html')

@app.route('/mp1')
def mp1():
    return render_template('mp1/index.html')  # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/data')
def data():
    load_src("stocks","py/stock_scraper.py")
    from stocks import get_data
    return jsonify(get_data())

@app.route('/images')
def imagest():
    load_src("imageSingle", "py/imageSingle.py")
    from imageSingle import get_image_data
    return jsonify(get_image_data())

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

