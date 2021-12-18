from flask import Flask
from flask import render_template
from flask import request
from werkzeug.exceptions import HTTPException
import requests

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uri = request.form.get('uri')
        html = get_uri(uri)
        return render_template('index.html', uri=uri, html=html)
    return render_template('index.html', uri='', html='')

def get_uri(uri):
    return requests.get(uri).text

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', e=e)

if __name__ == '__main__':
   app.run()