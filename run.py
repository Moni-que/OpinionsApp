from flask import Flask, render_template
app = Flask(__name__)



posts = [

    {
        'author': 'shee',
        'title': 'first opinion',
        'contents': 'firstcontent',
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


if __name__ == '__main__':
    app.run(debug = True)

