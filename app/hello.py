import os
import flask
from flask import Flask
from flask.ext.cors import CORS
import subprocess
import time

app = Flask(__name__)
CORS(app)

EAST_HOST = 'ec2-user@ec2-52-72-154-92.compute-1.amazonaws.com'
WEST_HOST = 'ec2-user@ec2-52-25-12-43.us-west-2.compute.amazonaws.com'

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

def sshcmd(host, cmd):
  com = "/usr/bin/ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no {} '{}'".format(host, cmd)
  return subprocess.Popen(com1, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")

@app.route("/cmd")
def runcommand():
  return sshcmd(EAST_HOST, 'ls')

@app.route("/check")
def runcheck():
  result1 = sshcmd(EAST_HOST, 'sh check.sh')
  result2 = sshcmd(WEST_HOST, 'sh check.sh')
  return "{}\n{}".format(result1, result2)

@app.route("/westmaster")
def oregonmaster():
  result1 = sshcmd(EAST_HOST, 'sh switch1.sh')
  time.sleep(2)
  result2 = sshcmd(WEST_HOST, 'sh switch1.sh')
  return "{}\n{}".format(result1, result2)

@app.route("/eastmaster")
def eastmaster():
  result1 = sshcmd(WEST_HOST, 'sh switch2.sh')
  time.sleep(2)
  result2 = sshcmd(EAST_HOST, 'sh switch2.sh')
  return "{}\n{}".format(result1, result2)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)