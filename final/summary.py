# Marvin Leon cs430
# This class manages the music summary functionality

from flask.views import MethodView

class musicSummary(MethodView):
    def get(self):
        return "<p>Hello,world</p>"