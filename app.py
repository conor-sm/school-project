from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz/<quiz_name>')
def quiz(quiz_name):
    return render_template(f'{quiz_name}.html')

if __name__ == '__main__':
    app.run(debug=True)