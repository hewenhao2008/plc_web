import sae
import os, sys
root = os.path.dirname(__file__)
from .web import wsgi
application = sae.create_wsgi_app(wsgi.application)