from flask import Flask, send_file

from generate_extension import generate_extension


app = Flask(__name__)



@app.route('/')
def index():
    filepath = 'extensions/' + generate_extension() + '.zip'
    return send_file(filepath)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    