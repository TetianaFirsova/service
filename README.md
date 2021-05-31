# service
web service (Restful) for CRUD operations (part of my final project)
[![Coverage Status](https://coveralls.io/repos/github/TetianaFirsova/service/badge.svg)](https://coveralls.io/github/TetianaFirsova/service)

See **[service specification](/documentation/SPECIFICATION.md)**
The web service is deployed on Heroku with name &quot;depemp-service&quot; and available at [https://depemp-service.herokuapp.com/](https://depemp-service.herokuapp.com/)


### How to run the project locally:

#### 0. Before you begin:
- Make sure you have **Python3.x** installed on your system.
- Install **PostgreSQL** database if you don't have it installed already.
- Make sure **virtualenv** is installed on your system.

#### 1. Clone the project from Github into new directory:
      $ git clone https://github.com/TetianaFirsova/service.git
    
#### 2. Open up your terminal and CD (change directory) into the app root folder 'service'. Create a virtual environment
	> python -m venv env
and activate it
	> env\Scripts\activate (for Windows) 
or
	$ source env/bin/activate (for Linux)

#### 3. Install all dependencies:
From your terminal, make sure you are in the root folder of the project then run the below command:
	> pip install -r requirements.txt
This will download and install all the extensions in [requirements.txt](/requirements.txt)

#### 4. Setting up configuration
Change the following code in [config.py](/config.py):
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1974tanya5@localhost/departments_db_1'
You need to replace the above values with the appropriate values of 'username', 'password', 'database_name' for your database by the rules:
	SQLALCHEMY_DATABASE_URI ="postgresql://username:password@localhost/database_name"

#### 5. Set configuration variables:
  - set FLASK_CONFIG=development (for Windows) 
or
  - export FLASK_CONFIG=development (for Linux)

#### 6. Run the project:
	>  python run.py

After running the service you could visit http://127.0.0.1:5002/api/departments or another endpoint, see [service specification](/documentation/SPECIFICATION.md)