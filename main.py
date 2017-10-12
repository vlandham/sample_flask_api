# -*- coding: utf-8 -*-
'''
App Entry Point
'''
from __future__ import print_function
# import os
import logging

from flask_restplus import cors
from flask_restplus import Resource


# Import Configured Flask App
from ds_api.app import app

# Import namespaces
from ds_api.endpoints.experiments import EXPERIMENTS_NS

# API is defined here
from ds_api.rest_api import API
from ds_api.data import db

ROOT = logging.getLogger()
ROOT.setLevel(logging.DEBUG)

# This provides CORS for all API Requests and adds in our media type coercing
# based on `format`
# API.decorators = [cors.crossdomain(origin='*')]

# Add namespaces defined in endpoints module
API.add_namespace(EXPERIMENTS_NS)

# init API with Flask App
API.init_app(app)

db.init_app(app)

DEBUG_FLAG = True
# API_MODE = os.environ.get("API_MODE")
print(__name__)
if __name__ == '__main__':
    print('running ')
    app.run(port=4411, debug=DEBUG_FLAG)
