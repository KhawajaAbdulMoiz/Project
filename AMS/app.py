from flask import Flask, render_template

app = Flask(__name__)
@app.route('/signup')
def signup():
    return render_template('signupform.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('loginpage.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)

