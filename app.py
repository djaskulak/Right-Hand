from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/itemsavailable')
def info():
    return render_template('pagetwo.html')


@app.route('/submittal')
def job():
    return render_template('thirdpage.html')


@app.route('/apply')
def apply():
    return render_template('apply.html')


# -------------------------------- END -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
