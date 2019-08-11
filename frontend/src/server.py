import requests, os
from flask import Flask, render_template, request, redirect, url_for

RESULTS_API_SERVER = os.environ['RESULTS_API_SERVER']
app = Flask(__name__)

# this will run on local computer on http://0.0.0.0:5000
@app.route('/')
def show_dishes():
    # RESULTS_API_SERVER is where the results-api is running within its container
    Dishes = requests.get(RESULTS_API_SERVER + "/show").json()  
    # rendering html template using Solutions (response from api) as an argument to use in template, under name solutions
    return render_template('show_dishes.html', dishes=Dishes)


@app.route('/add_dishes', methods=['GET', 'POST'])
def add_dishes():
    if request.method == 'GET':
        # when page first loads, render template that allows user to input value for N
        return render_template('add_dishes.html')
    else:
        # send post request with value of n as a json for api to add solutions to db
        json = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'category': request.form['category']
        }
        response = requests.post(RESULTS_API_SERVER + "/add", json=json)
        # checking solutions have been correctly added
        if response.status_code == 200:
            # redirect to view solutions we just added
            return redirect(url_for('show_dishes'))  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')