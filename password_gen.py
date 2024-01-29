import random
import string

letter = string.ascii_letters
digits = string.digits
punctuations = string.punctuation

def generate_password(has_letter, has_digit, has_punc, pwd_length=5):
    allpwd = []
    if has_letter:
        allpwd += letter
    if has_digit:
        allpwd += digits
    if has_punc:
        allpwd += punctuations
    
    pwd = ""
    
    for _ in range(pwd_length):
        pwd += random.choice(allpwd)
        return pwd
        