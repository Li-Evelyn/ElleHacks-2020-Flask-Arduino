from flask import Flask, render_template
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
def home():
    return "Go to /unlock to unlock your bike and /lock to lock your bike!"

@app.route('/unlock')
def unlock():
    time.sleep(0.5)
    change_lock_state("open")
    return 'Unlocked!'

@app.route('/lock')
def lock():
    time.sleep(0.5)
    change_lock_state("close")
    return 'Locked!'


if __name__ == '__main__':
    app.run()
