# N Queens #
My solution to the N-Queens puzzle, in the form of a full-stack Python app, Dockerized and tested with Travis CI and Pytest.

## Description ##
  Fun intro to Python and Docker-Compose, producing an extensively-tested CRUD app with an API container that uses SQLAlchemy to store all N Queens solutions for a given N (where N <= 12) into a PostgreSQL image running in a seperate container and a surprise Front-End container that uses Flask to send requests to the API image and shows all solutions using a Bootstrap template. On command, Docker-Compose builds and runs all services seperately for seperation of concerns and without the need to install dependencies or worry about your local setup.


## Requirements ##
  docker-compose version 3.3 
  
  On Windows and Mac it comes with [Docker 1.8](https://docs.docker.com/toolbox/toolbox_install_windows/), on Linux it must be installed seperately


## How to Get Started ##
  Ater cloning repo, build docker containers by running the following commands from root directory:
    
  ```bash
  docker-compose build
  docker-compose up
  ```


## Usage ##
  HTTP requests can be sent to api server on 127.0.0.1:5001

  Only tested for up to 12 queens.

  Example post request with curl to add solutions for 10 queens: 

  ```bash
  curl -XPOST -H "Content-type: application/json" -d \'{"n": "10"}' \'127.0.0.1:5001/add'
  ```

  Once added, all solutions can be viewed on [http://127.0.0.1:5001/show](http://127.0.0.1:5001/show)

  Bonus client-side for easier interaction with api on [http://127.0.0.1:5000](http://127.0.0.1:5000)


## Trigger Testing / Travis CI Build ##
  Any merge requests from this repo to origin master branch of this repo will trigger the Travis CI build which uses Pytest to: 
  
    - Run parallel tests on Python 2.7, 3.5 and 3.6 
  
    - Run parametrized tests on functions used to build and check the boards for the solutions to confirm that they produce the correct amount of solutions for a given N and every board is a valid solution for that N.
  
    - Test that the api is able to produce all solutions for N=10, store each one correctly in db, query them from db, manipulate them properly and send them back.

## Roadmap 
  > Next version will include tests to confirm there are no duplicate solutions per function call on N-Queens and also run parallel tests on Python 3.7, MacOS and Windows 10.
  
  > Will also manipulate the single list produced for each solution in order to store each solution board in the database as a matrix.