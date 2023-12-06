# Marvin Leon cs430
# This class manages the music track data functionality

from flask.views import MethodView
from flask import render_template, redirect
from util import get_token
import spotipy
import os

class GetTracks(MethodView):
    def get(self):
        try: 
            token_info = get_token()
        except: 
            print("user not logged in")
            return redirect("/")
        sp = spotipy.Spotify(auth=token_info['access_token'])
        current_user_name = sp.current_user()['display_name']

        if os.path.exists(".cache"): 
            os.remove(".cache")

        return render_template('summary.html', user_display_name=current_user_name, short_term=short_term, medium_term=medium_term, long_term=long_term, currentTime=gmtime())
