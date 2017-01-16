from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "secretashell"


@app.route('/')
def guessnumber():

    if 'guess' not in session:
        session['guess'] = 0
        session['truth'] = 1
        session['answer'] = random.randrange(0, 101)

    return render_template("index.html")



@app.route('/guess', methods=["post"])
def guesser():
    session['guess'] = request.form['guess']
    guess = int(session['guess'])
    ans = int(session['answer'])

    if guess > ans:
        session['truth'] = 2
    elif guess < ans:
        session['truth'] = 3
    else:
        session['truth'] = 0

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
