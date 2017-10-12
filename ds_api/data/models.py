from ds_api.data import db

from flask_restplus import fields
from ds_api.rest_api import API

ExperimentApi = API.model('Experiment', {
    "ZID": fields.Integer(readOnly=True, description='Experiment ZId')
})

ExperimentsApi = API.model('Experiments', {
    "results": fields.List(fields.Nested(ExperimentApi))
})

class Experiment(db.Model):
    zid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Experiment %r>' % self.name
