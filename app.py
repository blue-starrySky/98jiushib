from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,ssl_context=('2153883_xn--5vrwma.com.pem', '2153883_xn--5vrwma.com.key'))
