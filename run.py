from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='6c25c3e654c961bf5e1b1b54be43bc9d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_path = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(50), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_path}')"

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted =  db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"





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


if __name__ == '__main__':
    app.run(debug = True)

