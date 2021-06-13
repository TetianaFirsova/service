from run import db
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Department(db.Model):
    """
    create DB model for department
    """
    __tablename__ = 'department'

    id_dep = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(50))
    description = db.Column(db.String(300))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __init__(self, dep_name, description):
        self.dep_name = dep_name
        self.description = description

class DepartmentSchema(ma.Schema):
    """
    define Schema for Department class
    """
    id_dep = fields.Integer()
    dep_name = fields.String()
    description = fields.String()
