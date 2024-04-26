from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['age'] = request.form['age']
        session['language'] = request.form['language']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'name' in session:
        return f"Welcome {session['name']} to the Treasure Hunt!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
