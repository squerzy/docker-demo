from flask import Flask
import os

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

port = os.environ.get('PORT', 8080)

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=port) 
