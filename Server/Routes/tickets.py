from Routes import connection
from flask import Response, request, Blueprint
import QueryBuilder

tickets_bp = Blueprint('tickets', __name__)
qb = QueryBuilder.QueryBuilder()

@tickets_bp.route("/tickets", methods=["GET"])
def get_tickets():
    result = qb.select("tickets").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@tickets_bp.route("/tickets/<int:id>", methods=["GET"])
def get_ticket(id):
    result = qb.select("tickets").where(f"id = {id}").execute()
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
        qb.insert("tickets", ['PRICE', 'PROMOTION_ID', 'STATUS', 'TYPE', 'VALIDITY_END', 'VALIDITY_START'], [price, promotion_id, status, type_, validity_start, validity_end]).execute()
        return Response("Ticket successfully created and inserted in the database.", 201)
    except:
        print("An exception occurred when creating ticket")
        return Response(status=500)
