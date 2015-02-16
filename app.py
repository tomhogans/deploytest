import queue

from flask import Flask
app = Flask(__name__)

my_queue = queue.Queue()

with open("data.txt") as f:
    for s in f.read().splitlines():
        my_queue.put(s)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
