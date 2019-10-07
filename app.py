from flask import Flask

app = Flask(__name__)

@app.route('/') # the method is GET by default
def home():
    return 'Hello, World', 200

if __name__ == '__main__':
    app.run(debug=True)