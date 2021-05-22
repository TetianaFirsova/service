from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
from resources.Hello import Hello
api.add_resource(Hello, '/Hello')

from resources.departments import DepartmentsResource
api.add_resource(DepartmentsResource, '/departments')

from resources.employees import EmployeesResource
api.add_resource(EmployeesResource, '/employees')