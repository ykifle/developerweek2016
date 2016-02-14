import os
import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/mapdata")
def mapdata():
  data = { "count": 10785236,
   "photos": [
      {"photo_id": 27932,
      "photo_title": "Atardecer en Embalse",
      "photo_url": "http://www.panoramio.com/photo/27932",
      "photo_file_url": "http://mw2.google.com/mw-panoramio/photos/medium/27932.jpg",
      "longitude": -64.404945,
      "latitude": -32.202924,
      "width": 500,
      "height": 375,
      "upload_date": "25 June 2006",
      "owner_id": 4483,
      "owner_name": "Miguel Coranti",
      "owner_url": "http://www.panoramio.com/user/4483"}
  ]};
  return flask.jsonify(**data)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)