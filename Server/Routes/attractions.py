from app import app
from Routes import connection
from flask import Response, Blueprint

attractions_bp = Blueprint('attractions', __name__)

@attractions_bp.route("/attractions", methods=["GET"])
def get_all_attractions():
    result = connection.get_all_json("attractions")
    if not result:
        return Response(status=404)
    else:
        return result

@attractions_bp.route("/attractions/<int:id>", methods=["GET"])
def get_attraction_by_id(id):
    result = connection.get_by_id_json("attractions", id)
    if not result:
        return Response(status=404)
    else:
        return result
