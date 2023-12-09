# Marvin Leon cs430
# This file sets up Flask application and URL rules. It defines
# - initializes the Flask app (main entry point to the app)
# - defines the two primary enpoints, and binds them to presenter classes
# - utilizes Flask's MethodView that separates HTTP methods

import flask
from .views import Index, Login, Redirect, GetTracks
from .credentials import SECRET_KEY

app = flask.Flask(__name__)
app.secret_key= SECRET_KEY

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/redirect', view_func=Redirect.as_view('redirectPage'))
app.add_url_rule('/getTracks', view_func=GetTracks.as_view('getTracks'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
