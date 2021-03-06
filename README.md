# Taco's Place
Practice App that will allow user to select from a list of dishes and generate a detailed receipt


## Description ##
  API running on Docker container using SQLAlchemy performs CRUD operations on dishes in a seperate PostgreSQL database image. App is currently allowing user to add new dishes to the database and redirects to the page displaying all dishes.


## Requirements ##
  **Docker-Compose version 3.3**   
  - On Windows and Mac, Docker-Compose is included when installing [Docker Desktop](https://docs.docker.com/docker-for-windows/install/). 
  
  - On Linux, [Docker Engine](https://docs.docker.com/compose/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) must be installed seperately, in that order.

  - On command, Docker-Compose will build and run all services seperately for seperation of concerns and without the need to install dependencies or worry about your local setup.


## How to Get Started ##
  Just clone repo and load the docker containers by running the following commands:
    
  ```bash
  git clone https://github.com/yidahc/python-challenge.git
  cd python-challenge
  docker-compose build
  docker-compose up
  ```
  Build reports for all containers will appear on your terminal along with test results from pytest image 
  

## Usage ##
  HTTP requests can be sent to api server on 127.0.0.1:5001

  All dishes can be viewed on [http://127.0.0.1:5001/show](http://127.0.0.1:5001/show)

  Client-side for easier interaction with api on [http://127.0.0.1:5000](http://127.0.0.1:5000)

    
## Documentation and References Used

### Front-End and Python
- https://www.w3schools.com/python
- https://www.programiz.com/python-programming
- https://getbootstrap.com/docs/4.0/components/forms/
- https://getbootstrap.com/docs/4.0/examples/grid/

### Pytest
- https://docs.pytest.org/en/latest/getting-started.html#getstarted
- https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg
- https://github.com/cuenca-mx/clabe-python/blob/master/test_clabe.py

### Postgres and SQLAlchemy
- https://vsupalov.com/flask-sqlalchemy-postgres/
- https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/?fbclid=IwAR2YYvFgPMvGfEIeFPSVsZ0XvIQCWpvzAWhcMr0lU-9jNL9ndvbbU3pPluQ
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

### Docker and Travis CI
- https://medium.com/@audretschjames/understanding-docker-as-if-it-were-a-gameboy-96c96392efbf
- https://docs.docker.com/samples/library/postgres/
- https://linuxhint.com/run_postgresql_docker_compose/
- https://medium.com/@hmajid2301/implementing-sqlalchemy-with-docker-cb223a8296de
- https://www.smartfile.com/blog/testing-python-with-travis-ci/
- https://docs.travis-ci.com/user/job-lifecycle/#customizing-the-installation-phase