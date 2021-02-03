from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# -------------------------------- END -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=3000)
