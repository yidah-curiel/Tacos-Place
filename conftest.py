import pytest
import requests, os

RESULTS_API_SERVER = os.environ['RESULTS_API_SERVER']

# pytest fixture that adds solutions to db for n=10 using api and retrieves all solutions from db using api
@pytest.fixture
def supply_results():

  json = {
          'n': '10'
      }
  # merged front-end code for each seperate task
  response = requests.post(RESULTS_API_SERVER + "/add", json=json)
  if response.status_code == 200:
    Solutions = requests.get(RESULTS_API_SERVER + "/show").json()  
    # should return list of dictionaries with all the solutions from the db
    return Solutions


# pytest learned from https://docs.pytest.org/en/latest/getting-started.html#getstarted
# and https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg