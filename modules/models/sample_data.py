from modules.db_model import db
from sqlalchemy import Column, String, INTEGER
from typing import Dict

class SampleData(db.Model):
    __tablename__ = "sample"
    Id = db.Column(INTEGER(), primary_key=True)
    Data = db.Column(String(255), nullable=True)

    def serialize(self) -> Dict:
        vals = self.__dict__
        r_vals = vals.copy()
        for v in vals:
            if v[0] == '_':
                del r_vals[v]
        return r_vals

    def __init__(self, data=None):
        self.Data = data

    def __repr__(self):
        return '<Sample Data %r>' % self.Id
