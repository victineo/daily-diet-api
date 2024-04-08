from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(400), nullable=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=True) # HH:MM format
    isOnDiet = db.Column(db.Boolean, default=False)

    def to_dict(self): #Serializa a instância do Meal para um dicionário JSON.
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'time': self.time,
            'isOnDiet': self.isOnDiet
        }