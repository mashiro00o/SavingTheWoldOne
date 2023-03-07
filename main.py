from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    numbers = [1, 2, 3, 4, 5]
    with open('intro.txt', 'r') as file:
      msg = file.read()
    if request.method == 'POST':
      data = request.form['whatever']
      with open('secret.txt', 'a') as file: #save data permenatly
        file.write(data + '\n')
    return render_template('index.html', whatever=data, nums=numbers, intro=msg)

app.run(host='0.0.0.0', port=81)
