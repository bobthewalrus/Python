from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secretAF"

@app.route('/')
def countincrement():
    if session.has_key('count'):
        session['count']=session['count']+1
    else:
        session['count']=0
    return render_template("index.html")


@app.route('/two')
def two():
	session['count'] = session['count'] + 1
	return redirect('/')

@app.route('/reset')
def reset():
	session['count'] = 0
	return redirect('/')
app.run(debug=True)

# self.add2= Button(self.buttonClick,text="Submit", command=buttonClick)
