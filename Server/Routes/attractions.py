from flask import request
from flask import Response, Blueprint
import QueryBuilder

attractions_bp = Blueprint('attractions', __name__)
qb = QueryBuilder.QueryBuilder()

@attractions_bp.route("/attractions", methods=["GET"])
def get_all_attractions():
    try:
        status = request.args.get('status')
        type_ = request.args.get('type')

        query = qb.select("attractions")
        filters = []
        if status:
            filters.append(f"status = \'{status}\'")
        if type_:
            filters.append(f"type = \'{type_}\'")

        if filters:
            query = query.where(" AND ".join(filters))

        result = query.execute()

        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@attractions_bp.route("/attractions/<int:id>", methods=["GET"])
def get_attraction_by_id(id):
    try:
        result = qb.select("attractions").where(f"id = {id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)
