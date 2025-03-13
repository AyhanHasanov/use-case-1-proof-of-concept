from flask import Response, Blueprint
import QueryBuilder

attractions_bp = Blueprint('attractions', __name__)
qb = QueryBuilder.QueryBuilder()

@attractions_bp.route("/attractions", methods=["GET"])
def get_all_attractions():
    result = qb.select("attractions").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@attractions_bp.route("/attractions/<int:id>", methods=["GET"])
def get_attraction_by_id(id):
    result = qb.select("attractions").where(f"id = {id}").execute()
    if not result:
        return Response(status=404)
    else:
        return result
