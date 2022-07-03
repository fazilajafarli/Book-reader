from crypt import methods
from flask import Flask, render_template, request, redirect
import requests
import pyttsx3
from app import *
from models import *
from forms import *

@app.route('/', methods=['GET', 'POST'])
def home():
  post_data = request.form
  form = Text2Audio()
  if request.method == 'POST':
    form = Text2Audio(data = post_data)
    if form.validate_on_submit():
       engine = pyttsx3.init()
       engine.say("I will speak this text")
       engine.runAndWait()