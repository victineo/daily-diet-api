# daily-diet-api
Diet control API repository, made with Python, Flask and SQLite.

## Observation
When cloning this repository into your PC, go to 'app.py' and modify the brute path to the database according to the path where yours is stored in, to make sure it will run properly. Using the brute path instead of `sqlite:///database.db` was the solution I've found to make the application work as it should.