# Marvin Leon cs430
# This class manages the music track data functionality

from flask.views import MethodView
from flask import render_template, redirect, url_for
from your_module import get_token 
import spotipy

class GetTracks(MethodView):
    def get(self):
        try: 
            token_info = get_token()
        except: 
            print("user not logged in")
            return redirect("/")
        sp = spotipy.Spotify(auth=token_info['access_token'])
        # ... rest of your code ...