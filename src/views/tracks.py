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

        #gets the top tracks of the user , returns a dictionary
        short_term = sp.current_user_top_artists(
            limit=1,
            offset=0,
            time_range=SHORT_TERM,
        )
        medium_term = sp.current_user_top_artists(
            limit=1,
            offset=0,
            time_range=MEDIUM_TERM,
        )
        long_term = sp.current_user_top_tracks(
            limit=1,
            offset=0,
            time_range=LONG_TERM,
        )

        if os.path.exists(".cache"): 
            os.remove(".cache")
        
        genre = get_genre(medium_term) 
        
        chatReply = get_chat_reply(genre)
        
        if genre == 0:
            chatReply = "Sorry an error occurred with chatGPT"

        return render_template('music.html', user_display_name=current_user_name, short_term=genre, medium_term=medium_term, long_term=long_term, currentTime=gmtime(), chat_response=chatReply)

def get_genre(music_data):
    """
    Extracts and cleans the genre from the given Spotify data dictionary.

    Parameters:
    data (dict): A dictionary containing Spotify artist data.

    Returns:
    str: The cleaned genre of the artist.
    """
    genre_list = music_data['items'][0]['genres']
    if genre_list:
        # Extract the main genre, assuming it follows a pattern like 'pov: genre'
        genre = genre_list[0].split(':')[-1].strip()
        return genre
    else:
        return "0"

