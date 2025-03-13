from flask import Response, Blueprint
import QueryBuilder

events_bp = Blueprint('events', __name__)
qb = QueryBuilder.QueryBuilder()

@events_bp.route("/events", methods=["GET"])
def get_all_events():
    result = qb.select("special_events").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event_by_id(id):
    result = qb.select("special_events").where(f"id = {id}").execute()
    if not result:
        return Response(status=404)
    else:
        return result
