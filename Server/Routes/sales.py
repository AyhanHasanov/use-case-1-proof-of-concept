from app import app
from flask import Response, Blueprint
from Routes import connection

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/sales", methods=["GET"])
def get_all_sales():
    result = connection.get_all_json("sales")
    if not result:
        return Response(status=404)
    else:
        return result

@sales_bp.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    result = connection.get_by_id_json("sales", id)
    if not result:
        return Response(status=404)
    else:
        return result

