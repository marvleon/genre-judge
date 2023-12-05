# Marvin Leon cs430
# This class manages the music summary functionality

from flask.view import MethodView

class musicSummary(MethodView):
    def get(self):
        return "<p>Hello,world</p>"