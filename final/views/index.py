# Marvin Leon cs430
# MVP view component that handles the GET request for the home page
# Renders the homepage

from flask import render_template
from flask.views import MethodView

#This class  is a Flask view for the index page
class Index(MethodView):
    #Retrieves all entries from the model and renders them using index.html 
    def get(self):
        name = 'visitor!'
        return render_template("index.html", title='Welcome', username=name)
