'''
Created on Oct 10, 2015

@author: catzhangy1
'''
import db2
import ast
import notify

from flask import Flask, render_template, flash, redirect, url_for, Blueprint, request, g
import json
import os
import requests
import urllib
import base64

'''Configuring local Postgres Database on Shell
postgres -D /usr/local/var/postgres -- starts up postgrespo
createuser admin -- create admin user
createdb -U admin testdb'''

app = Flask(__name__)
    
@app.route('/search', methods=['GET'])
def testMethod3():
    return db2.flask_field_query(db2.connect_db())

@app.route('/notify', methods=['POST'])
def emailSO():
    data = ast.literal_eval(request.data)
    print data;
    print data[0];
    print data[1];
    print data[2];
    notify.funtimes(db2.connect_db(), data[1], data[2], data[0])
    return 'success'

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = ast.literal_eval(request.data)
    db = db2.connect_db()
    db2.insert_into_db(db, [tuple(data)], "contact_list")
    return 'success'

@app.route("/")
def main():
    return render_template('index.html', name='hello')

if __name__ == "__main__":
    app.run(debug=True)
