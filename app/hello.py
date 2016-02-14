import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/mapdata")
def mapdata():
  data = { "count": 10785236,
    "photos": [
      {"photo_id": 27932, "photo_title": "Atardecer en Embalse", "photo_url": "http://www.panoramio.com/photo/27932", "photo_file_url": "http://mw2.google.com/mw-panoramio/photos/medium/27932.jpg", "longitude": -64.404945, "latitude": -32.202924, "width": 500, "height": 375, "upload_date": "25 June 2006", "owner_id": 4483, "owner_name": "Miguel Coranti", "owner_url": "http://www.panoramio.com/user/4483"},
      {"photo_id": 522084, "photo_title": "In Memoriam Antoine de Saint Exupéry", "photo_url": "http://www.panoramio.com/photo/522084", "photo_file_url": "http://mw2.google.com/mw-panoramio/photos/medium/522084.jpg", "longitude": 17.470493, "latitude": 47.867077, "width": 500, "height": 350, "upload_date": "21 January 2007", "owner_id": 109117, "owner_name": "Busa Péter", "owner_url": "http://www.panoramio.com/user/109117"},
      {"photo_id": 1578881, "photo_title": "Rosina Lamberti,Sunset,Templestowe , Victoria, Australia", "photo_url": "http://www.panoramio.com/photo/1578881", "photo_file_url": "http://mw2.google.com/mw-panoramio/photos/medium/1578881.jpg", "longitude": 145.141754, "latitude": -37.766372, "width": 500, "height": 474, "upload_date": "01 April 2007", "owner_id": 140796, "owner_name": "rosina lamberti", "owner_url": "http://www.panoramio.com/user/140796"},
      {"photo_id": 97671, "photo_title": "kin-dza-dza", "photo_url": "http://www.panoramio.com/photo/97671", "photo_file_url": "http://mw2.google.com/mw-panoramio/photos/medium/97671.jpg", "longitude": 30.785408, "latitude": 46.639301, "width": 500, "height": 375, "upload_date": "09 December 2006", "owner_id": 13058, "owner_name": "Kyryl", "owner_url": "http://www.panoramio.com/user/13058"}
    ]
  }
  return flask.jsonify(**data)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)