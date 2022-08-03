from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

favoritosPersonajes = db.Table('favoritosPersonajes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('personajes_id', db.Integer, db.ForeignKey('personajes.id'), primary_key=True),
)

favoritosPlanetas = db.Table('favoritosPlanetas',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planetas_id', db.Integer, db.ForeignKey('planetas.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(300), unique=False, nullable=False)
    favoritosPersonajes = db.relationship('Personajes',secondary = favoritosPersonajes,backref =db.backref('favoritesPersonajes',lazy = True))
    favoritosPlanetas = db.relationship('Planetas',secondary = favoritosPlanetas,backref =db.backref('favoritesPlanetas',lazy = True))


def __repr__(self):
        return '<User %r>' % self.email

def serialize(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email,
            "FavoritosPersonajes": self.favoritosPersonajes,
            "favoritosPlanetas": self.favoritosPlanetas,
            # do not serialize the password, its a security breach
        }
    
def obtener_Favoritos(self):
        return list(map(lambda obj: obj.serialize(), self.Favoritos))

def obtener_favoritosPlanet(self):
        return list(map(lambda obj: obj.serialize(), self.favoritosPlanet))

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    forma = db.Column(db.String(250),  unique=False, nullable=False)
    características= db.Column(db.String(80), unique=False, nullable=False)
    especies_que_habitan = db.Column(db.String(250), unique=False, nullable=False)
    # personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'))
    # favoritos = db.relationship('Favorito',secondary= favoritos)
    def serialize(self):
        return {
            "id": self.id,
            "forma": self.forma,
            "características": self.caracteríticas,
    }


class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250),  unique=False, nullable=False)
    altura = db.Column(db.String(250),  unique=False, nullable=False)
    personalidad = db.Column(db.String(250),  unique=False, nullable=False)
    genero = db.Column(db.String(250),  unique=False, nullable=False)
    características= db.Column(db.String(80), unique=False, nullable=False)
    # favoritos = db.relationship('Favorito',secondary= favoritos)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "colorPelo": self.colorPelo,
            "colorOjos": self.colorOjos,
    }