from app import app
from Routes import connection
from flask import Response, Blueprint

events_bp = Blueprint('events', __name__)

@events_bp.route("/events", methods=["GET"])
def get_all_events():
    result = connection.get_all_json("special_events")
    if not result:
        return Response(status=404)
    else:
        return result

@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event_by_id(id):
    result = connection.get_by_id_json("special_events",id)
    if not result:
        return Response(status=404)
    else:
        return result
