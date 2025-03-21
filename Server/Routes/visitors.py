from flask import Response, Blueprint
from flask import request
from QueryBuilder import QueryBuilder

qb = QueryBuilder()
visitors_bp = Blueprint('visitors', __name__)

@visitors_bp.route("/visitors", methods=["GET"])
def get_all_visitors():
    try:
        # pointless to filter because all 3 attributes (name, email, phone) are expected to be unique for each visitor
        result = qb.select("visitors").execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@visitors_bp.route("/visitors/<int:id>", methods=["GET"])
def get_visitor_by_id(id):
    try:
        result = qb.select("visitors").where("id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)


@visitors_bp.route("/visitors", methods=["POST"])
def create_visitor():
    try:
        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        qb.insert("visitors", ['NAME', 'EMAIL', 'PHONE'], [name, email, phone]).execute()
        return Response(status=201)
    except:
        print("An exception occurred when creating visitor")
        return Response(status=500)

@visitors_bp.route("/visitors/<int:id>", methods=["PUT"])
def update_visitor_by_id(id):
    try:
        result = qb.select("visitors").where(f"id =", id).execute()
        if not result:
            return Response(status=404)

        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        (qb.update("visitors", ['NAME', 'EMAIL', 'PHONE'], [f"\'{name}\'", f"\'{email}\'", f"\'{phone}\'"])
        .where("id =", id).print_query()
        .execute())
        return Response(status=200)
    except:
        return Response(status=500)

@visitors_bp.route("/visitors/<int:id>", methods=["DELETE"])
def delete_visitor_by_id(id):
    try:
        result = qb.select("visitors").where("id =", id).execute()
        if not result:
            return Response(status=404)

        qb.delete("visitors").where("id =", id).execute()
        return Response(status=200)
    except:
        return Response(status=400)
