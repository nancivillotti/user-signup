from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('usersignup.html')

@app.route("/", methods=['POST'])
def signin():
    password_error = ""
    verify_error = ""
    username_error = ""
    email_error = ""

    password = request.form['password']
    verify = request.form['verify']
    username = request.form['username']
    email = request.form['email']


    if password == "":
        password_error = "Need password"
    
    if username == "":
        username_error = "Need username"
    

    if len(password)<3 or len(password)>20 or  (" " in password):
        password_error = "Enter valid password: password must be at least three characters and less than twenty characters. No spaces"
    
    if len(username)<3 or len(username)>20 or  (" " in username):
        username_error = "Enter valid username: username must be at least three characters and less than twenty characters. No spaces"

    if not password==verify:
        verify_error = "passwords must match. Do it over."
    

    if not email == "":
        if not ("@" in email) or not ('.' in email) or len(email)<3 or len(email)>20:
            email_error = 'Enter valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('usersignup.html', email = email, username = username, username_error = username_error, password_error= password_error, verify_error = verify_error, email_error = email_error)

app.run()