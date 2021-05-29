## Service description

&quot;service&quot; is a web service designed for the &quot;my\_department\_REST&quot; web application. It&#39;s a REST web service for CRUD operations.

The resources exposed by this service are departments and employees.

The REST API endpoints for the service are:

![ScreenShot](/documentation/endpoints.png)

The web service is deployed on Heroku with name &quot;depemp-service&quot; and available at [https://depemp-service.herokuapp.com/](https://depemp-service.herokuapp.com/)

The development server is listening for requests on port 5002 of the local host, so one could access it as [http://127.0.0.1:5002](http://127.0.0.1:5002/)

Web service returns data stored in the Postgres database.

Departments resource is composed of the following data fields:

- **id\_dep** : unique number of the department. Integer type.
- **dep\_name** : name of the department. String type.
- **description** : short department description. String type.

Data fields of employees resource are the following:

- **id\_emp** : unique number of the employee. Integer type.
- **first\_name** : name of the employee. String type.
- **last\_name** : sourname of the employee. String type.
- **birth\_date** : employee&#39;s date of birth. Date type.
- **salary** : employee&#39;s salary. Integer type.
- **department\_id** : id of department where employee works. Integer type.
- **email** : employee&#39;s e-mail address. String type.

Resources are represented by URIs. The client send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

To test the web service one should use the REST-clients, for example _curl_. It allows you to execute any HTTP methods for the desired resource. For example to test departments resource we can use the following curl command:

$ curl -i -H &quot;Content-Type: application/json&quot; -X POST -d &#39;{&quot;dep\_name&quot;:&quot;test faculty&quot;, &quot;description&quot;: &quot;test department description&quot;}&#39; http://depemp-service.herokuapp.com/api/departments

$ curl -i http://depemp-service.herokuapp.com/api/departments/1

$ curl -i http://depemp-service.herokuapp.com/api/departments

$ curl -X PUT -H &#39;Content-Type: application/json&#39; -d &#39;{&quot;id\_dep&quot;: 1, {&quot;dep\_name&quot;:&quot;new faculty&quot;, &quot;description&quot;: &quot;new description&quot;}&#39; http://depemp-service.herokuapp.com/api/departments

$ curl -X DELETE -H &#39;Content-Type: application/json&#39; -d &#39;{&quot;id\_emp&quot;: 1}&#39; http:// depemp-service.herokuapp.com/api/departments

where **-X** _[METHOD]_ defines HTTP method, **-d** _&quot;name=value&quot;_ sets the name and values of variables in POST/PUT, **-H** _[HEADER]_ sets the header, **-i** displays response headers.