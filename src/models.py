from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    eye = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    height = db.Column(db.String(250))
    personajes_id = db.relationship('Favoritos')

    def __repr__(self):
        return '<Personajes %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye": self.eye,
            "gender": self.gender,
            "height": self.height,
            }
    
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    planetas_id = db.relationship('Favoritos')

    def __repr__(self):
        return '<Planetas %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            
            }
    
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    user_id = db.relationship('Favoritos')

    def __repr__(self):
        return '<Usuarios %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            
            }


class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    personajes_id = db.Column(db.Integer,db.ForeignKey('personajes.id'))


    def __repr__(self):
        return '<Favoritos %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planetas_id": self.planetas_id,
            "personajes_id": self.personajes_id,
            
            }
