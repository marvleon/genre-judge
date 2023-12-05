# Marvin Leon cs430
# Manager for adding new entries to the database
# Renders the submission form
# Processes submitted entries

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import qmodel

#Flask view for managing entries
class Quote(MethodView):
    #renders a form to add a new entry (`add_quote.html`) 
    def get(self):
        return render_template("add_quote.html")
    #processes the submitted form data to insert a new entry into
    #the database and redirects to the index page
    def post(self):
        model = qmodel.get_model()
        model.insert(
            request.form["quote"],
            request.form["author"],
            request.form["source"],
            request.form["date"],
        )
        return redirect(url_for("index"))
