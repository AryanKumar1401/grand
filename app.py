from flask import Flask, render_template, url_for, request, redirect
import requests
import json

from requests.api import get

app = Flask('app')



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"]
    return quote

@app.route('/')
def hello(): 
    quote = get_quote()
    return render_template("homepage.html",quote=quote)









