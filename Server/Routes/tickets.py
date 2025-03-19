from flask import Response, request, Blueprint
from QueryBuilder import QueryBuilder

tickets_bp = Blueprint('tickets', __name__)
qb = QueryBuilder()

@tickets_bp.route("/tickets", methods=["GET"])
def get_tickets():
    try:
        ticket_type = request.args.get("type")
        ticket_status = request.args.get("status")

        result = qb.select("tickets").where("status =", ticket_status).and_where("type =", ticket_type).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@tickets_bp.route("/tickets/<int:id>", methods=["GET"])
def get_ticket(id):
    try:
        result = qb.select("tickets").where("id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@tickets_bp.route("/tickets", methods=["POST"])
def create_ticket():
    try:
        request_data = request.json
        price = request_data["PRICE"]
        promotion_id = request_data["PROMOTION_ID"]
        ticket_status = request_data["STATUS"]
        ticket_type = request_data["TYPE"]
        validity_end = request_data["VALIDITY_END"]
        validity_start = request_data["VALIDITY_START"]
        qb.insert("tickets", ['PRICE', 'PROMOTION_ID', 'STATUS', 'TYPE', 'VALIDITY_END', 'VALIDITY_START'], [price, promotion_id, ticket_status, ticket_type, validity_start, validity_end]).execute()
        return Response("Ticket successfully created and inserted in the database.", 201)
    except:
        print("An exception occurred when creating ticket")
        return Response(status=500)
