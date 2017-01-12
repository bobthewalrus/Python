from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def results():
    name = request.form['Name']
    location = request.form['Location']
    language = request.form['Language']
    comment = request.form['Comment']
    return render_template("results.html",name=name, location=location, language=language, comment=comment)
app.run(debug=True)
