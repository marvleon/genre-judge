# Marvin Leon cs430
# This file sets up Flask application and URL rules. It defines
# - initializes the Flask app (main entry point to the app)
# - defines the two primary enpoints, and binds them to presenter classes
# - utilizes Flask's MethodView that separates HTTP methods

import flask
from flask.views import MethodView
from login import Login
from redirect import RedirectPage
from summary import MusicSummary

app = flask.Flask(__name__)
#REPLACE ME!!!!!!!!!!!!!!!!!!!!!!!!
CLIENT_ID=9010a36dc457457187884f22cc60a67f
CLIENT_SECRET=75768b26e27d4ead84e842f235499fbb

def createSpotifyOuath():
    return SpotifyOAuth(
        clientID=CLIENT_ID,
        clientSecret=CLIENT_SECRET,
        redirect_uri=url_for("redirectPage", _external=True)
        scope="user-top-read user-library-read"
    )

app.add_url_rule("/receipt", view_func=Receipt.as_view("receipt"), methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
