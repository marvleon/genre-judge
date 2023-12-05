# Marvin Leon cs430
# This file sets up Flask application and URL rules. It defines
# - initializes the Flask app (main entry point to the app)
# - defines the two primary enpoints, and binds them to presenter classes
# - utilizes Flask's MethodView that separates HTTP methods

import flask
from flask.views import MethodView
from index import Index
from login import Login
from redirect import RedirectPage
from tracks import GetTracks
from summary import MusicSummary
from credentials import SECRET_KEY

app = flask.Flask(__name__)


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
