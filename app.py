from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', title="My 1st Webpage")

@app.route('/about')
def about():
    return render_template('about.html', title="About - My 1st Webpage")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact - My 1st Webpage")

@app.route('/technology')
def technology():
    return render_template('technology.html', title="Technology - My 1st Webpage")

if __name__ == '__main__':
    app.run(debug=True)



