import socketio
sio = socketio.Client()

@sio.event
def connect():
    print("接続")

sio.connect("http://localhost:5000")