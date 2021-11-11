from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Web App with Python Flask!'

if __name__ == '__main__':
	application.run(host='', port=5000)