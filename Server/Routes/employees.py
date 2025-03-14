from flask import request
from flask import Response, Blueprint
import QueryBuilder

employees_bp = Blueprint('employees', __name__)
qb = QueryBuilder.QueryBuilder()

@employees_bp.route("/employees", methods=["GET"])
def get_all_employees():
    try:
        job_id = request.args.get('job_id')
        dep_id = request.args.get('dep_id')
        query = qb.select("employees")

        filters = []
        if job_id:
            filters.append(f"job_id = {job_id}")
        if dep_id:
            filters.append(f"dep_id = {dep_id}")

        if filters:
            query = query.where(" AND ".join(filters))

        result = query.execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@employees_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    try:
        result = qb.select("employees").where(f"id = {id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)
