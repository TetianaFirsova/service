from flask import request
from flask_restful import Resource
from datetime import datetime


class EmployeesResource(Resource):
    def get(self):
        from models.employee import Employee, EmployeeSchema
        employees_schema = EmployeeSchema(many=True)

        employees = Employee.query.all()
        employees = employees_schema.dump(employees)
        return {'status': 'success', 'data': employees}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.employee import Employee, EmployeeSchema
        employee_schema = EmployeeSchema()

        try:
            data = employee_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST

        from models.department import Department
        department_id = Department.query.filter_by(id_dep=data['department_id']).first()
        if not department_id:
            return {'status': 'error', 'message': 'department for this employee not found'}, 422

        employee = Employee.query.filter_by(last_name=data['last_name'], email=data['email']).first()
        if employee:
            return {'message': 'Department already exists'}, 400

        employee = Employee(
            first_name=json_data['first_name'],
            last_name=json_data['last_name'],
            birth_date=json_data['birth_date'],
            salary=json_data['salary'],
            department_id=json_data['department_id'],
            email=json_data['email']
            )
        
        from run import db
        db.session.add(employee)
        db.session.commit()

        result = employee_schema.dump(employee)

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.employee import Employee, EmployeeSchema
        employee_schema = EmployeeSchema()

        try:
            data = employee_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST

        from models.department import Department
        department_id = Department.query.filter_by(id_dep=data['department_id']).first()
        if not department_id:
            return {'status': 'error', 'message': 'department for this employee not found'}, 422

        employee = Employee.query.filter_by(id_emp=data['id_emp']).first()
        if not employee:
            return {'message': 'Employee does not exist'}, 400
        if data['first_name']:
            employee.first_name = data['first_name']
        if data['last_name']:
            employee.last_name = data['last_name']
        if data['birth_date']:
            employee.birth_date = data['birth_date']
        if data['salary']:
            employee.salary = data['salary']
        if data['department_id']:
            employee.department_id = data['department_id']
        if data['email']:
            employee.email = data['email']
        from run import db
        db.session.commit()

        result = employee_schema.dump(employee)

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.employee import Employee, EmployeeSchema
        employee_schema = EmployeeSchema()

        try:
            data = employee_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST

        employee = Employee.query.filter_by(id_emp=data['id_emp']).delete()
        from run import db
        db.session.commit()

        result = employee_schema.dump(employee)

        return { "status": 'success', 'data': result}, 204


class EmployeeResource(Resource):
    def get(self, id):
        from models.employee import Employee, EmployeeSchema
        employee_schema = EmployeeSchema()

        employee = Employee.query.filter_by(id_emp=id).first()
        if not employee:
            return {'status': 'failed', 'message': 'Employee does not exist'}, 400
        result = employee_schema.dump(employee)

        return { "status": 'success', 'data': result}, 200


class EmployeesSearch(Resource):
    def get(self, search_birth_date):
        from models.employee import Employee, EmployeeSchema
        employees_schema = EmployeeSchema(many=True)

        try:
            birth_date_obj=datetime.strptime(str(search_birth_date), '%Y-%m-%d')
        except ValueError as err:
            return {'message': "Invalid birth date format"}

        if birth_date_obj:
            employees = Employee.query.filter_by(birth_date=search_birth_date).all()

        if not employees:
            return {'status': 'failed', 'message': 'Employee mathing your date does not exist'}, 400

        employees = employees_schema.dump(employees)
        return {'status': 'success', 'data': employees}, 200

class EmployeesPeriodSearch(Resource):
    def get(self, start_birth_date, end_birth_date):
        from models.employee import Employee, EmployeeSchema
        employees_schema = EmployeeSchema(many=True)

        try:
            start_birth_date_obj=datetime.strptime(str(start_birth_date), '%Y-%m-%d')
            end_birth_date_obj=datetime.strptime(str(end_birth_date), '%Y-%m-%d')
        except ValueError as err:
            return {'message': "Invalid birth dates format"}

        if start_birth_date_obj.date() and end_birth_date_obj.date():
            employees = Employee.query.filter(Employee.birth_date.between(start_birth_date, end_birth_date)).all()
        
        if not employees:
            return {'status': 'failed', 'message': 'Employee mathing your dates does not exist'}, 400

        employees = employees_schema.dump(employees)
        return {'status': 'success', 'data': employees}, 200