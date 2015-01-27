
# import the Flask class from the flask module
from flask import Flask, render_template, jsonify
from utilities import load_src

# create the application object
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('mainPage.html')

# Generic route for exercises
@app.route('/<exType>/<exName>')
def ex(exType,exName):
    wholeName = exType + '_' + exName
    load_src("exCode", 'py/' + wholeName + '/compute.py')
    from exCode import do_compute
    do_compute() #writes json file that wholeName/index.html reads
    return render_template(wholeName + '/index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

