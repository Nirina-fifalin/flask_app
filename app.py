#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/bonjour/<username>')
def bonjour_user(username):
    return 'Bonjour %s!\n' % username

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s!\n' % username

@app.route('/au-revoir/<username>')
def au_revoir_user(username):
    return 'Au revoir %s?\n' % username

# Route de test pour valider le pipeline CI/CD non?
@app.route('/feature')
def feature():
    return 'Feature!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# Test final du pipeline CI/CD (feature1)