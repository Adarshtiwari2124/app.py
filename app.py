mkdir flaskapp && cd flaskapp
nano app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from AWS Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

sudo python3 app.py
