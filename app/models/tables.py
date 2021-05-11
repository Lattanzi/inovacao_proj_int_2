from app import db

#tabela de usuarios
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username





#tabela de clientes/pacientes
class Cliente(db.Model):
    __tablename__ = "clientes"

    id_cli = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    cliente = db.Column(db.String)
    telefone = db.Column(db.String)
    email_cli = db.Column(db.String(120), unique=True, nullable=False)


    def __init__(self, cpf, cliente, telefone, email_cli):
        self.cpf = cpf
        self.cliente = cliente
        self.telefone = telefone
        self.email_cli = email_cli

    def __repr__(self):
        return "<Cliente %r>"
