from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('thank_you', name=name))

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')
    return f"Thank you, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
