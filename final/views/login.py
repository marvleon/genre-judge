# Marvin Leon cs430
# This class manages the login functionality

from flask.views import MethodView
from flask import redirect
from ..util import create_spotify_oauth

class LoginView(MethodView):
    def get(self):
        sp_oauth = create_spotify_oauth()
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
