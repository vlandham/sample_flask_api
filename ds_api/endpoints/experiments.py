# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
'''
Routes focused on experiments.
'''

from flask import request
from flask_restplus import Resource

from ds_api.rest_api import API
from ds_api.data.models import ExperimentsApi
from ds_api.data.models import Experiment

EXPERIMENTS_NS = API.namespace('experiments', description='Experiment specific API')


@EXPERIMENTS_NS.route('/')
class Experiments(Resource):
    '''
    Experiments List
    '''
    # @API.expect(TYPE_ARGUMENTS)
    # @format_response(location_children_to_csv)
    @API.marshal_with(ExperimentsApi)
    def get(self):
        """
        Get experiments
        """

        # args = TYPE_ARGUMENTS.parse_args(request)

        # return Experiment.query()
        return {'results': [{'zid':1, 'name': 'a experiment'}]}
