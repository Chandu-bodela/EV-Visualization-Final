from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', msg=None)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"Contact from {name} <{email}>: {message}")
    return render_template('index.html', msg=f"Thanks {name}, your message has been received!")

if __name__ == '__main__':
    app.run(debug=True)
