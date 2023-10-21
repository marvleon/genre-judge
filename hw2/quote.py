# Marvin Leon cs430
# Manager for adding new entries to the database
# Renders the quote submission form
# Processes submitted quotes

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import qmodel

class Quote(MethodView):
    def get(self):
        return render_template('add_quote.html')

    def post(self):
        model = qmodel.get_model()
        model.insert(request.form['quote'], request.form['author'], request.form['source'], request.form['date'])
        return redirect(url_for('index'))
