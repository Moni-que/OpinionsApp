from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='6c25c3e654c961bf5e1b1b54be43bc9d'



posts = [

    {
        'author': 'shee',
        'title': 'first opinion',
        'content': 'firstcontent',
        'date_posted': '1 April 2018'
    },
    {
        'author': 'Kheshi',
        'title': 'second opinion',
        'content': 'secondcontent',
        'date_posted': '10 April 2018'
    }

]

@app.route("/")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account was successfully created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
    app.run(debug = True)

