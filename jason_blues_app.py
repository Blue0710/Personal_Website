from flask import Flask, render_template
import os
# app = Flask(__name__)
app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('index0515.html')


if __name__ == '__main__':
    app.run(debug=True)

