# Receiving input from whatsapp

from twilio.rest import Client
from flask import Flask , request
from stock_price import *
from database import *

app = Flask(__name__)

account_sid = 'your account_sid'
auth_token = 'your auth_token'
client = Client(account_sid, auth_token)

@app.route("/")
def hello():
    print("Hello!")
    return "hello!"

@app.route("/whatsapp", methods=['GET','POST'])
def whatsapp():
    message_received = request.form['Body']
    print(message_received)
    message_received = list(message_received.split(" "))
    input_data(message_received)
    return '200'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', use_reloader = True)
