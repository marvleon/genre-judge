# Marvin Leon cs430
# This class manages the login functionality

from flask.view import MethodView

class Login(MethodView):
    def get(self):
        sp_oath = create_spotify_oath()
        auth_url = sp_oath.get_authorize_url()
        return redirect(auth_url)