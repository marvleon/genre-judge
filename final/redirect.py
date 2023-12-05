# Marvin Leon cs430
# This class manages the redirect functionality

from flask.view import MethodView

class RedirectPage(MethodView):
    def get(self):
        sp_oauth = create_spotify_oauth()
        session.clear() 
        code = request.args.get('code')
        token_info = sp_oauth.get_access_token(code)
        session[TOKEN_CODE] = token_info    
        return redirect(url_for("getTracks", _external=True))