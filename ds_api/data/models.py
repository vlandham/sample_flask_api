from ds_api.data import db

from flask_restplus import fields
from ds_api.rest_api import API

ExperimentApi = API.model('Experiment', {
    "zid": fields.Integer(readOnly=True, description='Experiment ZId'),
    "name": fields.String(readOnly=True, description='Name')
})

ExperimentsApi = API.model('Experiments', {
    "results": fields.List(fields.Nested(ExperimentApi))
})


class Experiment(db.Model):
    zid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Experiment %r>' % self.name
