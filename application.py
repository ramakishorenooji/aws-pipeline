from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
	return 'This is a dev instance with the code verision 1.1, added via AWS pipeline for CI/CD activities'
	