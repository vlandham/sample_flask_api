# -*- coding: utf-8 -*-
'''
App Entry Point
'''
from __future__ import print_function
# import os
import logging

from flask_restplus import cors

# Import Configured Flask App
from ds_api.app import app

# Import namespaces
from ds_api.endpoints.experiments import EXPERIMENTS_NS

# API is defined here
from ds_api.rest_api import API

ROOT = logging.getLogger()
ROOT.setLevel(logging.DEBUG)

# This provides CORS for all API Requests and adds in our media type coercing
# based on `format`
API.decorators = [cors.crossdomain(origin='*')]


# init API with Flask App
API.init_app(app)

# Add namespaces defined in endpoints module
API.add_namespace(EXPERIMENTS_NS)

DEBUG_FLAG = True
# API_MODE = os.environ.get("API_MODE")
print(__name__)
if __name__ == 'main':
    print('running ')
    app.run(port=8080, debug=DEBUG_FLAG)
