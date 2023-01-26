from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

# Esta clase nos permite traer la información de todos los usuarios
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250) , nullable=False)
    password = db.Column(db.String(250) , nullable=False)
    email = db.Column(db.String(250), unique= True, nullable=False)
    
    # favorite = db.relationship('Favourite', backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
        }


        


# Esta clase nos permite importar todos los personajes de Star Wars

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String(250))

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "skin_color": self.skin_color,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column( db.String(250))
    climate = db.Column( db.String(250))
    population =  db.Column( db.Integer)
    orbital_period =  db.Column( db.Integer)
    rotation_period =  db.Column( db.Integer)
    diameter =  db.Column( db.Integer)
    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(250))
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    crew_capacity = db.Column(db.Integer)
    manufacturer = db.Column(db.String(250))
    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_name": self.vehicle_name,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "crew_capacity": self.crew_capacity,
            "manufacturer": self.manufacturer,
        }


class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id')) 
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'))
    character_id = db.Column(db.Integer, ForeignKey('character.id'))
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)
    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_name": self.vehicle_name,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "crew_capacity": self.crew_capacity,
            "manufacturer": self.manufacturer,
        }







class Favourites(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)
