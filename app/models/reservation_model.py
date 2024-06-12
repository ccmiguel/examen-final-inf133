from app.database import db


# Define la clase `Reservation` que hereda de `db.Model`
# `Reservation` representa la tabla `Reservations` en la base de datos
class Reservation(db.Model):
    __tablename__ = "reservations"

    # Define las columnas de la tabla `Reservations`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Reservation`
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    # Guarda un Reservation en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Reservationes de la base de datos
    @staticmethod
    def get_all():
        return Reservation.query.all()

    # Obtiene un Reservation por su ID
    @staticmethod
    def get_by_id(id):
        return Reservation.query.get(id)

    # Actualiza un Reservation en la base de datos
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()

    # Elimina un Reservation de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()