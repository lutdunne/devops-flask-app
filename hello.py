from flask import Flask
import redis, json, time

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
    html = '''
        <p>Welcome, I am a Flask app!</p>
        <p>
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a>
        </p>
    '''
    return html


@app.route('/about')
def about():
    cached = r.get('about')
    if cached is not None:
        data = json.loads(cached)
        if time.time() - data['time'] <= 600:
            return data['html']

    html = '''
        <p>This application is running on the Flask web framework.</p>
        <p>Learn more about <a href="https://flask.palletsprojects.com">Flask</a>.</p>
        <p><a href="/">Home</a> | <a href="/contact">Contact</a></p>
    '''
    r.set('about', json.dumps({'html': html, 'time': time.time()}))
    return html


@app.route('/contact')
def contact():
    return '<p>My email is c23470466@mytudublin.ie</p><p><a href="/">Home</a></p>'
