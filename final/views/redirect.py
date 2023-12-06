# Marvin Leon cs430
# This class manages the redirect functionality

from flask import request, session, redirect, url_for
from flask.views import MethodView
from util import create_spotify_oauth
from credentials import TOKEN_CODE

class Redirect(MethodView):
    def get(self):
        sp_oauth = create_spotify_oauth()
        session.clear() 
        code = request.args.get('code')
        token_info = sp_oauth.get_access_token(code)
        session[TOKEN_CODE] = token_info    
        return redirect(url_for("getTracks", _external=True))