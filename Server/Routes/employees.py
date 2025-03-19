from flask import request
from flask import Response, Blueprint
from QueryBuilder import QueryBuilder

employees_bp = Blueprint('employees', __name__)
qb = QueryBuilder()

@employees_bp.route("/employees", methods=["GET"])
def get_all_employees():
    try:
        job_id = request.args.get('job_id')
        dep_id = request.args.get('dep_id')

        result = qb.select("employees").where("job_id =", job_id).and_where("department_id =", dep_id).execute()

        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@employees_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    try:
        result = qb.select("employees").where(f"id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)
