from flask import flask, render_template, request

app=flask(__name__)

@app.route('/')
def firstPage():
    return render_template('SurveyForm.html')

