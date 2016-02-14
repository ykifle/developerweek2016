import os
import flask
from flask import Flask
from flask.ext.cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/mapdata")
def mapdata():
  data = { "count": 2,
   "nodes": [
      {
        "name": "US-West",
        "longitude": -122.431297,
        "latitude": 37.7833,
        "id": 1,
        "master": True
      },
      {
        "name": "US-East",
        "longitude": -73.138260,
        "latitude": 40.792240,
        "id": 2,
        "master": False
      }
  ]};
  return flask.jsonify(**data)

@app.route("/cmd")
def runcommand():
  com = "/usr/bin/ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ec2-user@ec2-52-72-154-92.compute-1.amazonaws.com 'ls'"
  proc = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE)
  return proc.stdout.read()

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)