import os
import socket

from flask import Flask, render_template
from redis import Redis, RedisError

# Connect to Redit
redis = Redis(host='redis', db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = os.getenv('NAME', "world")

    hostname = socket.gethostname()

    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "cannot connect to Redis, counter disabled"

    return render_template('index.html', name=name, hostname=hostname, visits=visits)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
