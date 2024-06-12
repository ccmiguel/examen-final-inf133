from flask import Blueprint, jsonify, request

from app.models.restaurant_model import Restaurant
from app.utils.decorators import jwt_required, roles_required
from app.views.restaurant_view import render_restaurant_detail, render_restaurant_list

# Crear un blueprint para el controlador de restaurantes
restaurant_bp = Blueprint("restaurant", __name__)


# Ruta para obtener la lista de restaurantos
@restaurant_bp.route("/restaurants", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_restaurants():
    restaurants = Restaurant.get_all()
    return jsonify(render_restaurant_list(restaurants))


# Ruta para obtener un restaurant específico por su ID
@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if restaurant:
        return jsonify(render_restaurant_detail(restaurant))
    return jsonify({"error": "Restauranto no encontrado"}), 404


# Ruta para crear un nuevo restaurant
@restaurant_bp.route("/restaurants", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_restaurant():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Validación simple de datos de entrada
    if not name or not description or not price or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo restaurant y guardarlo en la base de datos
    restaurant = Restaurant(name=name, description=description, price=price, stock=stock)
    restaurant.save()

    return jsonify(render_restaurant_detail(restaurant)), 201


# Ruta para actualizar un restaurant existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_restaurant(id):
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "Restauranto no encontrado"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Actualizar los datos del restaurant
    restaurant.update(name=name, description=description, price=price, stock=stock)

    return jsonify(render_restaurant_detail(restaurant))


# Ruta para eliminar un restaurant existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_restaurant(id):
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "Restauranto no encontrado"}), 404

    # Eliminar el restaurant de la base de datos
    restaurant.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204