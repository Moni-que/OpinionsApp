from flask import render_template, url_for, flash, redirect, request
from MyOpinionsApp import app, db, bcrypt
from MyOpinionsApp.models import User, Post
from MyOpinionsApp.forms import RegistrationForm, LoginForm
from flask_login import login_user

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
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account was successfully created! ,You can now proceed to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful', 'danger')
    return render_template('login.html', title = 'Login', form = form)