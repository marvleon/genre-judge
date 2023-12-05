# Marvin Leon cs430
# This class manages the login functionality

from flask.view import MethodView

class Login(MethodView):
    def spotifyLogin():
        sp_oauth = SpotifyOAuth(
            clientID=CLIENT_ID,
            clientSecret=CLIENT_SECRET,
            redirect_uri=url_for("redirectPage", _external=True)
            scope="user-top-read user-library-read"
        )
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
