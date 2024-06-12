from flask import Blueprint, jsonify, request

from app.models.reservation_model import Reservation
from app.utils.decorators import jwt_required, roles_required
from app.views.reservation_view import render_reservation_detail, render_reservation_list

# Crear un blueprint para el controlador de reservationes
reservation_bp = Blueprint("reservation", __name__)


# Ruta para obtener la lista de reservationos
@reservation_bp.route("/reservations", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_reservations():
    reservations = Reservation.get_all()
    return jsonify(render_reservation_list(reservations))


# Ruta para obtener un reservation específico por su ID
@reservation_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_reservation(id):
    reservation = Reservation.get_by_id(id)
    if reservation:
        return jsonify(render_reservation_detail(reservation))
    return jsonify({"error": "Reservationo no encontrado"}), 404


# Ruta para crear un nuevo reservation
@reservation_bp.route("/reservations", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_reservation():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Validación simple de datos de entrada
    if not name or not description or not price or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo reservation y guardarlo en la base de datos
    reservation = Reservation(name=name, description=description, price=price, stock=stock)
    reservation.save()

    return jsonify(render_reservation_detail(reservation)), 201


# Ruta para actualizar un reservation existente
@reservation_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_reservation(id):
    reservation = Reservation.get_by_id(id)

    if not reservation:
        return jsonify({"error": "Reservationo no encontrado"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Actualizar los datos del reservation
    reservation.update(name=name, description=description, price=price, stock=stock)

    return jsonify(render_reservation_detail(reservation))


# Ruta para eliminar un reservation existente
@reservation_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_reservation(id):
    reservation = Reservation.get_by_id(id)

    if not reservation:
        return jsonify({"error": "Reservationo no encontrado"}), 404

    # Eliminar el reservation de la base de datos
    reservation.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204