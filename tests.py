import unittest
from flask_testing import TestCase
import datetime
from run import create_app, db
from run import app
from models.department import Department
from models.employee import Employee

service_url='/api/departments'
service_url_emp='/api/employees'

class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        
        return app
   
    def setUp(self):
        """
        Will be called before every test
        """
        self.client = app.test_client
        db.create_all()

        # create test departments
        dep_1 = Department(dep_name="test dep 1", description="testing department 1")
        dep_2 = Department(dep_name="test dep 2", description="testing department 2")
        dep_3 = Department(dep_name="test dep 3", description="testing department 3")

        # save deps to db
        db.session.add(dep_1)
        db.session.add(dep_2)
        db.session.add(dep_3)
        db.session.commit()

        # create test employees
        emp_1 = Employee(first_name="name1", last_name="sourname1", birth_date=datetime.date(2014, 3, 24), salary=5,
                         department_id=1, email="ghfghf@gmail.com")
        emp_2 = Employee(first_name="name2", last_name="sourname2", birth_date=datetime.date(2014, 10, 24), salary=50,
                         department_id=2,
                         email="gh44455@gmail.com")

        # save employees to database
        db.session.add(emp_1)
        db.session.add(emp_2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_department_model(self):
        """
        Test number of records in Department table
        """
        self.assertEqual(Department.query.count(), 3)

    def test_employee_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Employee.query.count(), 2)
        
class TestCRUDoperationsDepartment(TestBase):
    def test_department_creation(self):
        """
        Test API can create a department (POST request)
        """
        res = self.client().post(service_url, json={"dep_name": "test dep 4", "description": "testing department 4"})
        self.assertEqual(res.status_code, 201)
        self.assertIn('dep 4', str(res.data))

    def test_api_can_get_all_departments(self):
        """
        Test API can get a list of all departments(GET request)
        """
        res = self.client().get(service_url)
        self.assertEqual(res.status_code, 200)
        self.assertIn('dep 1', str(res.data))
        self.assertIn('dep 2', str(res.data))
        self.assertIn('dep 3', str(res.data))

    def test_api_can_get_department_by_id(self):
        """
        Test API can get a single department by it's id
        """
        res = self.client().get(service_url+'/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('dep 1', str(res.data))

    def test_department_can_be_edited(self):
        """
        Test API can edit an existing department (PUT request)
        """
        res = self.client().put(service_url, json={"id_dep": 1, "dep_name": "", "description": "this is a new description"})
        self.assertEqual(res.status_code, 204)
        results = self.client().get(service_url+'/1')
        self.assertIn('is a new', str(results.data))
        self.assertIn('dep 1', str(results.data))

    def test_department_deletion(self):
        """
        Test API can delete an existing department. (DELETE request)
        """
        res = self.client().delete(service_url, json={"id_dep": 1})
        self.assertEqual(res.status_code, 204)
        # Test to see if it exists, should return a 400
        result = self.client().get(service_url+'/1')
        self.assertEqual(result.status_code, 400)

class TestCRUDoperationsEmployee(TestBase):

    def test_api_can_get_all_employees(self):
        """
        Test API can get a list of all employees(GET request)
        """
        res = self.client().get(service_url_emp)
        self.assertEqual(res.status_code, 200)
        self.assertIn('name1', str(res.data))
        self.assertIn('name2', str(res.data))

    def test_api_can_get_employee_by_id(self):
        """
        Test API can get a single employee by it's id
        """
        res = self.client().get(service_url_emp+'/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('name1', str(res.data))

    def test_employee_deletion(self):
        """
        Test API can delete an existing employee. (DELETE request)
        """
        res = self.client().delete(service_url_emp, json={"id_emp": 1})
        self.assertEqual(res.status_code, 204)
        # Test to see if it exists, should return a 400
        result = self.client().get(service_url_emp+'/1')
        self.assertEqual(result.status_code, 400)

    def test_api_can_search_employee_by_birth_date(self):
        """
        Test API can search employee by birth date
        """
        res = self.client().get(service_url_emp+'/search/2014-10-24')
        self.assertEqual(res.status_code, 200)
        self.assertIn('name2', str(res.data))

    def test_api_can_search_employee_by_between_dates(self):
        """
        Test API can search employee by between two dates 
        """
        res = self.client().get(service_url_emp+'/search_between/2013-10-24,2014-10-24')
        self.assertEqual(res.status_code, 200)
        self.assertIn('name1', str(res.data))
        self.assertIn('name2', str(res.data))

    def test_api_Hello(self):
        res = self.client().get('/api/Hello')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Hello', str(res.data))
        
if __name__ == '__main__':
    unittest.main()