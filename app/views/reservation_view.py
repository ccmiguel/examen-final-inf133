def render_reservation_list(reservations):
    # Representa una lista de reservationes como una lista de diccionarios
    return [
        {
            "id": reservation.id,
            "name": reservation.name,
            "description": reservation.description,
            "price": reservation.price,
            "stock": reservation.stock,
        }
        for reservation in reservations
    ]


def render_reservation_detail(reservation):
    # Representa los detalles de un reservation como un diccionario
    return {
        "id": reservation.id,
        "name": reservation.name,
        "description": reservation.description,
        "price": reservation.price,
        "stock": reservation.stock,
    }