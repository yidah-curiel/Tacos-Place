import json
from app import create_app
from flask import request
from models import db, Dish

app = create_app()

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    category = data['category']

    entry = Dish(
    name = name,
    description = description,
    price = int(price),
    category = category
    )
    db.session.add(entry)
    # commit all additions to db
    db.session.commit()
    return json.dumps("Solutions Added"), 200

@app.route('/show', methods=["GET"])
# this will run on local computer on http://0.0.0.0:5001/show
def fetch():
    # query all entries(rows) in db
    dishes = Dish.query.all()
    all_dishes = []
    # iterate through queried solutions and 
    for dish in dishes:
        new_dish = {
            "name": dish.name,
            "description": dish.description,
            "price": dish.price,
            "category": dish.category
        }
    # restructure each class instance as dictionaries to store in all_dishes list
        all_dishes.append(new_dish)
    return json.dumps(all_dishes), 200
    # return list with nested dictionaries of all solutions as a json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
