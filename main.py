from flask import Flask, render_template, request
from password_gen import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password-generate', methods=['GET'])
def password():
    #veriler burada
    pwd_length = request.form.get('length')
    print(pwd_length)
    has_letter = request.form.get('letter')
    has_digit = request.form.get('digit')
    has_punc = request.form.get('punctuation')
    
    return render_template('password-generator.html',
                           pwd_length=pwd_length,
                           has_letter=has_letter,
                           has_digit=has_digit,
                           has_punc=has_punc)
    
@app.route('/password-generate/result')
def result(has_letter, has_digit, has_punc, pwd_length):
    return render_template('password-result.html',
                           result=generate_password(has_letter,
                                                    has_digit,
                                                    has_punc,
                                                    int(pwd_length)))
                           
app.run(debug=True)

    

    
    