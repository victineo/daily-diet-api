from flask import Flask, request, jsonify
from models.meal import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# BRUTE PATH TO THE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\GAMER\\Desktop\\codigos\\Rocketseat\\Python\\Módulo 4\\daily-diet-api\\instance\\database.db'

db.init_app(app)

@app.route('/view', methods=['GET'])
def view_meals():
    meals = Meal.query.all() # Searching for all the meals
    if meals: # If there are any meals
        return jsonify([m.to_dict() for m in meals]) # Return a list of dictionaries with the info of each meal in the DB
    else:
        return jsonify({'message': 'There is no meal to be shown yet.'}), 400 # Bad Request

@app.route('/view/<int:id_meal>', methods=['GET'])
def view_meal(id_meal):
    meal = Meal.query.get(id_meal) # Searching for the specific meal by its id
    if meal: # If this meal exists
        return jsonify(meal.to_dict()) # Return its info
    else:
        return jsonify({'message': 'Meal not found.'}), 404 # Not Found

@app.route('/create', methods=['POST'])
def create_meal():
    data = request.get_json() # Getting the data that was sent on JSON
    if 'name' in data and 'description' in data and 'date' in data and 'time' in data and 'isOnDiet' in data: # If the data contains all the required fields
        meal = Meal(**data) # Store this data in a new object of type Meal
        db.session.add(meal) # Add it to the session
        db.session.commit() # And save
        return jsonify({'message': 'Meal added successfully.'})
    else:
        return jsonify({'message': 'Failed to add meal.'}), 400 # Bad Request
    
@app.route('/edit/<int:id_meal>', methods=['PUT'])
def edit_meal(id_meal):
    data = request.get_json() # Getting the data that was sent on JSON
    meal = Meal.query.get(id_meal) # Searching for the meal we want to edit

    if not meal: # If there is no meal
        return jsonify({'message': 'Meal not found.'}), 404 # Not Found
    
    if 'name' in data: # If a 'name' field was sent on the JSON
        meal.name = data['name'] # Update the 'name' field on the desired meal
    if 'description' in data: # If a 'description' field was sent on the JSON
        meal.description = data['description'] # Update the 'description' field on the desired meal
    if 'date' in data: # If a 'date' field was sent on the JSON
        meal.date = data['date'] # Update the 'date' field on the desired meal
    if 'time' in data: # If a 'time' field was sent on the JSON
        meal.time = data['time'] # Update the 'time' field on the desired meal
    if 'isOnDiet' in data: # If an 'isOnDiet' field was sent on the JSON
        meal.isOnDiet = data['isOnDiet'] # Update the 'isOnDiet' field on the desired meal
    try:
        db.session.commit()
        return jsonify({'message': 'Meal updated successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Failed to update meal. Error: {str(e)}'}), 500 # Internal Server Error

@app.route('/delete:<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal) # Searching for the meal we want to edit

    if meal: # If the meal exists
        db.session.delete(meal) # Delete
        db.session.commit() # Save
        return jsonify({'message': 'Meal deleted successfully.'})
    else:
        return jsonify({'message': 'Meal not found.'}), 404 # Not Found

if __name__ == '__main__':
    app.run(debug=True)