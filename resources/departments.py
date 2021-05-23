from flask import request
from flask_restful import Resource


class DepartmentsResource(Resource):
    def get(self):
        from models.department import Department, DepartmentSchema
        departments_schema = DepartmentSchema(many=True)

        departments = Department.query.all()
        departments = departments_schema.dump(departments)
        return {'status': 'success', 'data': departments}, 200


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
            return {'message': 'Department does not exist'}, 400
        result = department_schema.dump(department)

        return { "status": 'success', 'data': result}, 200