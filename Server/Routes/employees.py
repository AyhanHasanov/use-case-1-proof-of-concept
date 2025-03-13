from app import app
from Routes import connection
from flask import Response, Blueprint

employees_bp = Blueprint('employees', __name__)

@employees_bp.route("/employees", methods=["GET"])
def get_all_employees():
    result = connection.get_all_json("employees")
    if not result:
        return Response(status=404)
    else:
        return result

@employees_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    result = connection.get_by_id_json("employees", id)
    if not result:
        return Response(status=404)
    else:
        return result
