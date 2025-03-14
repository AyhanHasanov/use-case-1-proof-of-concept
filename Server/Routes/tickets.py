from flask import Response, request, Blueprint
import QueryBuilder

tickets_bp = Blueprint('tickets', __name__)
qb = QueryBuilder.QueryBuilder()

@tickets_bp.route("/tickets", methods=["GET"])
def get_tickets():
    try:
        type_ = request.args.get("type")
        status = request.args.get("status")
        query = qb.select("tickets")

        filters = []
        if status:
            filters.append(f"status = \'{status}\'")
        if type_:
            filters.append(f"type = \'{type_}\'")

        if filters:
            query = query.where(f" AND ".join(filters))

        result = query.execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@tickets_bp.route("/tickets/<int:id>", methods=["GET"])
def get_ticket(id):
    try:
        result = qb.select("tickets").where(f"id = {id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

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
