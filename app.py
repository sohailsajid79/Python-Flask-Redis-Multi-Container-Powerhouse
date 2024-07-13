from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def hello():
    return "Welcome to my Flask web app"

@app.route('/count')
def counter():
    count = redis.incr('visitor_count')
    return f"Visitor count {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)