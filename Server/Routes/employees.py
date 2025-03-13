from flask import Response, Blueprint
import QueryBuilder

employees_bp = Blueprint('employees', __name__)
qb = QueryBuilder.QueryBuilder()

@employees_bp.route("/employees", methods=["GET"])
def get_all_employees():
    result = qb.select("employees").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@employees_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    result = qb.select("employees").where(f"id = {id}").execute()
    if not result:
        return Response(status=404)
    else:
        return result
