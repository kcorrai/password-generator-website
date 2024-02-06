from flask import Flask, render_template, request
from password_gen import generate_password

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#sqlite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#database oluşumu
db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.Integer, nullable=False)
    letter = db.Column(db.Boolean)
    digit = db.Column(db.Boolean)
    punctuation = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<User {self.id}>'
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password_generate')
def password():
    #veriler burada
    return render_template('password-generator.html')
    
        
    
@app.route('/password-generate/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        pwd_length = request.form['lenght']
        if request.form.get('letter'):
            has_letter = True
        else:
            has_letter = False
            
        if request.form.get('digit'):
            has_digit = True
        else:
            has_digit = False
            
        if request.form.get('punctuation'):
            has_punc = True
        else:
            has_punc = False
            
        pwd = Password(length=pwd_length, letter=has_letter, digit=has_digit, punctuation=has_punc)
        db.session.add(pwd)
        db.session.commit()
        

        return render_template('password-result.html',
                                result=generate_password(has_letter,has_digit,has_punc, int(pwd_length)))
        
    else:
        return render_template('password-result.html')
    
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()           
    app.run(debug=True)

    

    
    