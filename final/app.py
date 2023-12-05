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

app.add_url_rule("/summary", view_func=summary.as_view("summary"), methods=["GET"])
app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/redirect', view_func=Redirect.as_view('redirectPage'))
app.add_url_rule('/getTracks', view_func=GetTracks.as_view('getTracks'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
