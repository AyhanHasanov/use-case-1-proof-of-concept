from flask import Response, Blueprint
from flask import request
import QueryBuilder

events_bp = Blueprint('events', __name__)
qb = QueryBuilder.QueryBuilder()

@events_bp.route("/events", methods=["GET"])
def get_all_events():
    try:
        type_ = request.args.get("type")
        query = qb.select("special_events")

        if type_:
            query = query.where(f"type = \'{type}\'")

        result = query.execute()

        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event_by_id(id):
    try:
        result = qb.select("special_events").where(f"id = {id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)
