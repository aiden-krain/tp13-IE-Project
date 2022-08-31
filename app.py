from flask import Flask,  render_template,url_for
app = Flask(__name__)

@app.route('/')
def recommendation():
    return render_template('recommendation.html')

@app.route('/Home')
def home():
    #return render_template('recommendation.html')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)