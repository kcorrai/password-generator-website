from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password-generate', methods=['GET'])
def password():
    has_letter = request.get