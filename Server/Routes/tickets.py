from app import app
from Routes import connection
from flask import Response, request, Blueprint

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route("/tickets", methods=["GET"])
def get_tickets():
    result = connection.get_all_json("tickets")
    if not result:
        return Response(status=404)
    else:
        return result

@tickets_bp.route("/tickets/<int:id>", methods=["GET"])
def get_ticket(id):
    result = connection.get_by_id_json("tickets", id)
    if not result:
        return Response(status=404)
    else:
        return result

@tickets_bp.route("/tickets", methods=["POST"])
def create_ticket():
    try:
        request_data = request.json
        price = request_data["PRICE"]
        promotion_id = request_data["PROMOTION_ID"]
        status = request_data["STATUS"]
        type_ = request_data["TYPE"]
        validity_end = request_data["VALIDITY_END"]
        validity_start = request_data["VALIDITY_START"]
        query = f"INSERT INTO tickets(price, promotion_id, status, type, validity_start, validity_end) VALUES ({price}, {promotion_id}, '{status}', '{type_}', '{validity_start}', '{validity_end}');"
        connection.insert_query(query)
        return Response("Ticket successfully created and inserted in the database.", 201)
    except:
        print("An exception occurred when creating ticket")
        return Response(status=500)
