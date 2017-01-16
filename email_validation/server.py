from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key= "SecretShmecret"
mysql = MySQLConnector(app,'email_validation')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/emails')
def results():
    query = "select * from emails"
    emails = mysql.query_db(query)
    return render_template('index2.html',all_emails=emails)

@app.route('/emails/create_user', methods=['POST'])
def create():
    EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    check = request.form['emails']
    print check
    if len(check)<1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(check):
        flash('Invalid Email Address!')
    else:
        flash("Success!")
        query = "INSERT INTO emails (email, created_at, updated_at)VALUES (:emails, NOW(), NOW())"
        data = {
        'emails': request.form['emails'],
        }
        mysql.query_db(query, data)

    return redirect('/emails')
@app.route('/return')
def return1():
    return redirect('/')
@app.route('/remove_emails/<emails_id>', methods=['POST'])
def delete(emails_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': emails_id}
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
