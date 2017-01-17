from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
@app.route('/')
def index():
    query = "SELECT * FROM friend"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friend(first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<id>/edit')
def edit(id):
    print id
    query= "SELECT * FROM friend WHERE id= :id"
    data={"id":id}
    friend1=mysql.query_db(query,data)
    print "poop", friend1
    return render_template('index2.html', friend1=friend1)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friend SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friend WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
