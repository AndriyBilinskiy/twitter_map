
from flask import Flask,render_template,request
from main import main

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST'])
def data():
    if request.method == 'POST':
        form_data = request.form
        main(form_data["name"])
    return render_template('Map.html')
app.run(debug=True)