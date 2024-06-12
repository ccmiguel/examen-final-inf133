def render_restaurant_list(restaurants):
    # Representa una lista de restaurantes como una lista de diccionarios
    return [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "price": restaurant.price,
            "stock": restaurant.stock,
        }
        for restaurant in restaurants
    ]


def render_restaurant_detail(restaurant):
    # Representa los detalles de un restaurant como un diccionario
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "description": restaurant.description,
        "price": restaurant.price,
        "stock": restaurant.stock,
    }