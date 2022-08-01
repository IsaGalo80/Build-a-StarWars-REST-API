from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

favoritosPerson = db.Table('favoritosPerson',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('personajes_id', db.Integer, db.ForeignKey('Personajes.id'), primary_key=True)
)

favoritosPlanet = db.Table('favoritosPlanet',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('planetas_id', db.Integer, db.ForeignKey('Planetas.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(300), unique=False, nullable=False)
    favoritosPerson = db.relationship(personajes,
                    secondary=favoritosPerson,
                    lazy='subquery',
                    backref=db.backref('usuarios', lazy=True))
    favoritosPlanet = db.relationship(Planetas,
                    secondary=favoritosPlanet,
                    lazy='subquery',
                    backref=db.backref('usuarios', lazy=True))
    
    # user = db.relationship("User", secondary="favoritosPlanetPer")
def __repr__(self):
        return '<User %r>' % self.nickname

def serialize(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email,
            "favoritosPerson": self.obtener_favoritosPerson(),
            "favoritosPlanet": self.obtener_favoritosPlanet(),
            # do not serialize the password, its a security breach
        }
    
def obtener_favoritosPerson(self):
        return list(map(lambda obj: obj.serialize(), self.favoritosPerson))

def obtener_favoritosPlanet(self):
        return list(map(lambda obj: obj.serialize(), self.favoritosPlanet))

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    forma = db.Column(db.String(250),  unique=False, nullable=False)
    características= db.Column(db.String(80), unique=False, nullable=False)
    especies_que_habitan = db.Column(db.String(250), unique=False, nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'))
    planetas = db.relationship("Planetas", secondary= favoritosPlanet)
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
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "colorPelo": self.colorPelo,
            "colorOjos": self.colorOjos,
    }