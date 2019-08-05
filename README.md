# N Queens #

## My solution of the N-Queens challenge. ##

## AKA My first full-stack Python app, Dockerized and tested with Travis CI ##

## Summary ##
  > Give a summary of the product and the benefit. Assume the reader will not read anything else so make this paragraph good.

## Requirements ##
  > docker-compose version 3.5 
  > On Windows and Mac it comes with Docker, on Linux it must be installed seperately.
  > https://docs.docker.com/toolbox/toolbox_install_windows/

## How to Get Started ##
  > Ater cloning repo, build docker images by running the following commands from root directory:
  > - docker-compose build
  > - docker-compose up
  > - client-side


## Loading Solutions ##
  > Only tested for up to 12 queens.
  > HTTP requests can be sent to api server on 127.0.0.1:5001
  > Example to add solutions for 10 queens: curl -XPOST -H "Content-type: application/json" -d \'{"n": "10"}' \'127.0.0.1:5001/add'
  > Once added, all solutions can be viewed on 127.0.0.1:5001/show
  > Bonus client-side for easier interaction with api on http://127.0.0.1:5000

## Trigger Tests / CI Build ##
  > Any merge requests to origin master branch of this repo will trigger the Travis CI build which runs extensive tests on functions that produce the N Queens solutions.