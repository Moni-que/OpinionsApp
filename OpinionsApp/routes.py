from flask import render_template, url_for, flash, redirect, request
from OpinionsApp import app
from OpinionsApp.models import User, Post
from OpinionsApp.forms import RegistrationForm, LoginForm

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
@app.route("/home")
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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '12345':
            flash('log in successfullt', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful', 'danger')
    return render_template('login.html', title = 'Login', form = form)