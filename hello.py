from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''
<<<<<<< HEAD
        	<p>This is another string!</p>
=======
        	<p>Welcome!</p>
>>>>>>> new_greeting
        	<p><a href="/about">About</a> | <a href="/contact">Contact</a></p>
    	'''

@app.route('/about')
def about():
	return '<p>This app is running on the Flask web framework and <a href="htttps://www.python.ord">Python<a> <a href="https://flask.palletsprojects.com">Learn more about Flask</a></p>'

@app.route('/contact')
def contact():
    return '''
        <p>Contact me at: your-email@example.com</p>
        <p><a href="/">Home</a> | <a href="/about">About</a></p>
    '''
