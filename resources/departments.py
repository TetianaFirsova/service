from flask import request
from flask_restful import Resource


def avg_salary_and_dep_emps(depart):
    """
    returns all employees of department 'depart' and average salary for that employees 
    """
    from models.employee import Employee, EmployeeSchema
    employees_schema = EmployeeSchema(many=True)
    dep_employees=Employee.query.filter_by(department_id=depart.id_dep).all()
    if dep_employees:
        sum=0
        for emp in dep_employees:
            sum=sum+emp.salary
        avg_salary=sum/len(dep_employees)
        result1 = employees_schema.dump(dep_employees)
    else:
        avg_salary=0
        result1 = 'no employees'
    return result1, avg_salary

"""
class DepartmentsResource(Resource):
    def get(self):
        from models.department import Department, DepartmentSchema
        departments_schema = DepartmentSchema(many=True)

        departments = Department.query.all()
        departments = departments_schema.dump(departments)
        return {'status': 'success', 'data': departments}, 200
"""

class DepartmentsResource(Resource):
    def get(self):
        from models.department import Department, DepartmentSchema
        departments_schema = DepartmentSchema(many=True)

        departments = Department.query.all()
        avg_salary=[]
        for dep in departments:
            avg_salary.append(avg_salary_and_dep_emps(dep)[1])

        departments = departments_schema.dump(departments)
        return {'status': 'success', 'data': departments, 'avg_sal': avg_salary}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.department import Department, DepartmentSchema
        department_schema = DepartmentSchema()

        try:
            data = department_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST
        department = Department.query.filter_by(dep_name=data['dep_name']).first()
        if department:
            return {'message': 'Department already exists'}, 400
        department = Department(
            dep_name=json_data['dep_name'],
            description=json_data['description']
            )
        
        from run import db
        db.session.add(department)
        db.session.commit()

        result = department_schema.dump(department)

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.department import Department, DepartmentSchema
        department_schema = DepartmentSchema()

        try:
            data = department_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST

        department = Department.query.filter_by(id_dep=data['id_dep']).first()
        if not department:
            return {'message': 'Department does not exist'}, 400
        if data['dep_name']:
            department.dep_name = data['dep_name']
        if data['description']:
            department.description = data['description']
        from run import db
        db.session.commit()

        result = department_schema.dump(department)

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        from models.department import Department, DepartmentSchema
        department_schema = DepartmentSchema()

        try:
            data = department_schema.load(json_data)
        except ValidationError as exc:
            return {'message': "Validation errors", 'errors': exc.messages}, HTTPStatus.BAD_REQUEST

        department = Department.query.filter_by(id_dep=data['id_dep']).delete()
        from run import db
        db.session.commit()

        result = department_schema.dump(department)

        return { "status": 'success', 'data': result}, 204


class DepartmentResource(Resource):
    def get(self, id):
        from models.department import Department, DepartmentSchema
        department_schema = DepartmentSchema()

        department = Department.query.filter_by(id_dep=id).first()
        if not department:
            return {'status': 'failed', 'message': 'Department does not exist'}, 400
        
        result1, avg_salary = avg_salary_and_dep_emps(department)

        result = department_schema.dump(department)

        return { "status": 'success', 'dep_data': result, 'dep_employees': result1, 'average salary': avg_salary}, 200