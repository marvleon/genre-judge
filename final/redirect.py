# Marvin Leon cs430
# This class manages the redirect functionality

from flask.view import MethodView

class RedirectPage(MethodView):
    def pageRedirect():
        code = request.args.get('code') # pageRedirect?code=TOKEN, returns token
        sp_oath = SpotifyOAuth(
            clientID=CLIENT_ID,
            clientSecret=CLIENT_SECRET,
            redirect_uri=url_for("redirectPage", _external=True)
            scope="user-top-read user-library-read"
        )
        token_info = sp_oath.get_access_token(code)
        session[TOKEN_INFO] = token_info
        return redirect(url_for("summary", _external=True))