from flask import Flask
import serial
import time

app = Flask(__name__)

def change_lock_state(state):
    ser = serial.Serial('COM4', 9600)
    if state == "open":
        time.sleep(0.1)
        ser.write(b'H')
    else:
        time.sleep(0.1)
        ser.write(b'L')

@app.route('/')
def hello_world():
    change_lock_state("open")
    time.sleep(2)
    change_lock_state("")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
