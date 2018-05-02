from flask import Flask, render_template, flash, request
# from wtforms import Form, StringField
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# class ReusableForm(Form):
#    email = StringField('Enter your shared Spotify or Apple Music URI:')


@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template('index.html')


@app.route('/about')
def about():
        return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
