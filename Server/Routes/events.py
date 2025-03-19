from flask import Response, Blueprint
from flask import request
from QueryBuilder import QueryBuilder

events_bp = Blueprint('events', __name__)
qb = QueryBuilder()

@events_bp.route("/events", methods=["GET"])
def get_all_events():
    try:
        event_type = request.args.get("type")
        result = qb.select("special_events").where("type =", event_type).execute()

        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event_by_id(id):
    try:
        result = qb.select("special_events").where(f"id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)
