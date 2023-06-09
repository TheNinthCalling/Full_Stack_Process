from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def firstPage():
    return render_template('SurveyForm.html')

@app.route("/submit-form", methods=["POST"])
def submit_form():
    name = request.form['name']
    email = request.form['email']

    return redirect(url_for('second', name=name, email=email))

@app.route('/second')
def second():
    name = request.args.get('name')
    email = request.args.get('email')

    return render_template('second.html', name=name, email=email)
if __name__ == '__main__':
    app.run()
