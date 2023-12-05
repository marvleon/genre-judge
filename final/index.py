# Marvin Leon cs430
# MVP view component that handles the GET request for the home page
# Renders the homepage with quotes

from flask import render_template
from flask.views import MethodView
import qmodel

#This class  is a Flask view for the index page
class Index(MethodView):
    #Retrieves all entries from the model and renders them using index.html 
    def get(self):
        model = qmodel.get_model()
        entries = [
            dict(quote=row[0], author=row[1], source=row[2], date=row[3], added=row[4])
            for row in model.select()
        ]
        return render_template("index.html", entries=entries)
