from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

#default URL route saat flask run dieksekusi
@app.route('/')
def index():
    return render_template('index.html')

#alamat URL yang dituju saat menu "Home" diklik
@app.route('/index.html')
def index_html():
    return render_template('index.html')

#alamat URL yang dituju saat menu "SignUp" diklik
@app.route('/SignUp', methods = ['GET', 'POST'])
def SignUp(): 
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('pass')
        re_pass = request.form.get('re_pass')

        if password != re_pass:
            return "Password does not match, please try again !", 400
        
        print(f"Username: {username}, email: {email}, password: {password}")

        return redirect(url_for('index'))

    return render_template('SignUpUser.html')

@app.route('/SignIn', methods = ['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form.get('your_name')
        password = request.form.get('your_pass')

        if username =="admin" and password == "admin123":
            return render_template('Welcome.html', username="Admin")
        else:
            return render_template('Welcome.html', username=username)
    return render_template('SignInUser.html')

if __name__ == "__main__":
    app.run(debug=True)