from flask import request
from flask import Response, Blueprint
from QueryBuilder import QueryBuilder

attractions_bp = Blueprint('attractions', __name__)
qb = QueryBuilder()

@attractions_bp.route("/attractions", methods=["GET"])
def get_all_attractions():
    try:
        status = request.args.get('status')
        attraction_type = request.args.get('type')

        result = qb.select("attractions").where("status =", status).and_where("type =", attraction_type).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@attractions_bp.route("/attractions/<int:id>", methods=["GET"])
def get_attraction_by_id(id):
    try:
        result = qb.select("attractions").where("id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)
