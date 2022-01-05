# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/callback")
def get_yahoo_auth_url():
    return "<p>Hello, World!</p>"
    # url = "https://api.login.yahoo.com/oauth2/request_auth"
    # params =

"