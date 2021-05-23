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

from resources.employees import EmployeeResource
api.add_resource(EmployeeResource, '/employees/<int:id>')

from resources.departments import DepartmentResource
api.add_resource(DepartmentResource, '/departments/<int:id>')

from resources.employees import EmployeesSearch
api.add_resource(EmployeesSearch, '/employees/search/<search_birth_date>')

from resources.employees import EmployeesPeriodSearch
api.add_resource(EmployeesPeriodSearch, '/employees/search_between/<start_birth_date>,<end_birth_date>')