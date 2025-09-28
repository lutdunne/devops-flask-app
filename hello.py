from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!<p>'

@app.route('/about')
def about():
	return '<p>This app is running on the Flask web framework. <a href="https://flask.palletsprojects.com">Learn more about Flask</a></p>'
