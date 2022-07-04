from flask import Flask, render_template, request, redirect
import pyttsx3
import os
from werkzeug.utils import secure_filename
from app import *
from models import *
from forms import *

@app.route('/', methods=['GET', 'POST'])
def home():
  post_data = request.form
  form = UploadForm()
  if request.method == 'POST':
      form = UploadForm(data=post_data)
      if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(filename)))
        
        return redirect('/')
    #  engine = pyttsx3.init()
    #  engine.say()
    #  engine.runAndWait()

  return render_template('upload.html', form=form)
