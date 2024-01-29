from flask import Flask, render_template, request
from password_gen import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password_generate')
def password():
    #veriler burada
    return render_template('password-generator.html')
    
        
    
@app.route('/password-generate/result', methods=['POST'])
def result():
    pwd_length = request.form['lenght']
    if request.form['letter']:
        has_letter = True
    else:
        has_letter = False
        
    if request.form['digit']:
        has_digit = True
    else:
        has_digit = False
        
    if request.form['punctuation']:
        has_punc = True
    else:
        has_punc = False
    
    
    with open("kullanici-verisi.txt", "w") as f:
        f.write(pwd_length + ' | ')
        f.write(str(has_letter) + ' | ')
        f.write(str(has_digit) + ' | ')
        f.write(str(has_punc )+ ' | ')

    return render_template('password-generator.html',
                            result=generate_password(has_letter,has_digit,has_punc,int(pwd_length)))
    
                           
app.run(debug=True)

    

    
    