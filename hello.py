from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''
        	<p>Welcome!</p>
        	<p><a href="/about">About</a> | <a href="/contact">Contact</a></p>
    	'''

@app.route('/about')
def about():
	return '<p>This app is running on the Flask web framework. <a href="https://flask.palletsprojects.com">Learn more about Flask</a></p>'

@app.route('/contact')
def contact():
    return '''
        <p>Contact me at: your-email@example.com</p>
        <p><a href="/">Home</a> | <a href="/about">About</a></p>
    '''
