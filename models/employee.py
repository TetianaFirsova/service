from run import db
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Employee(db.Model):
    """
    create DB model for employee
    """
    __tablename__ = 'employee'

    id_emp = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    birth_date = db.Column(db.Date())
    salary = db.Column(db.Integer())
    department_id = db.Column(db.Integer, db.ForeignKey("department.id_dep"))
    email = db.Column(db.String(60), unique=True)

    def __init__(self, first_name, last_name, birth_date, salary, department_id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.salary = salary
        self.department_id = department_id
        self.email=email

class EmployeeSchema(ma.Schema):
    id_emp = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    birth_date = fields.DateTime()
    salary = fields.Integer()
    department_id = fields.Integer()
    email = fields.String()