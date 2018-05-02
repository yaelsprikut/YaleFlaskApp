from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    email = TextField('Enter your shared Spotify or Apple Music URI:')


@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    print form.errors
    if request.method == 'POST':
        example_input_email = request.form['exampleInputEmail1']
        # print example_input_email
        page = requests.get(example_input_email)
        soup = BeautifulSoup(page.content, 'html.parser')
        data = soup.find('title').get_text()
        print data


        if form.validate():
            # Save the comment here.
            flash('Your song is  ' + data)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('index.html', form=form)


@app.route('/about')
def about():
        return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)