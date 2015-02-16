import Queue

from flask import Flask
app = Flask(__name__)

my_queue = Queue.Queue()

with open("data.txt") as f:
    for s in f.read().splitlines():
        my_queue.put(s)

@app.route('/')
def next_item_from_queue():
    item = my_queue.get()
    my_queue.put(item)
    return item

if __name__ == '__main__':
    app.run()
