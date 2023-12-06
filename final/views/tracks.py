# Marvin Leon cs430
# This class manages the music track data functionality

from flask.views import MethodView
from flask import render_template, redirect
from ..util import get_token, SHORT_TERM, MEDIUM_TERM, LONG_TERM
from time import gmtime
import spotipy
import os
from ..chat import get_chat_reply
from ..credentials import OPENAI_API_KEY

class GetTracks(MethodView):
    def get(self):
        try: 
            token_info = get_token()
        except: 
            print("user not logged in")
            return redirect("/")
        sp = spotipy.Spotify(auth=token_info['access_token'])
        current_user_name = sp.current_user()['display_name']
        short_term = sp.current_user_top_tracks(
            limit=10,
            offset=0,
            time_range=SHORT_TERM,
        )
        medium_term = sp.current_user_top_tracks(
            limit=10,
            offset=0,
            time_range=MEDIUM_TERM,
        )
        long_term = sp.current_user_top_tracks(
            limit=10,
            offset=0,
            time_range=LONG_TERM,
        )

        if os.path.exists(".cache"): 
            os.remove(".cache")

        chatReply= get_chat_reply()

        return render_template('music.html', user_display_name=current_user_name, short_term=short_term, medium_term=medium_term, long_term=long_term, currentTime=gmtime(), chat_response=chatReply)
