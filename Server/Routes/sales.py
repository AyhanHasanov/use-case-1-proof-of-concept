from flask import Response, Blueprint
from flask import request
import QueryBuilder

sales_bp = Blueprint("sales", __name__)
qb = QueryBuilder.QueryBuilder()

@sales_bp.route("/sales", methods=["GET"])
def get_all_sales():
    try:
        product_id = request.args.get("product_id")
        employee_id = request.args.get("employee_id")
        visitor_id = request.args.get("visitor_id")

        query = qb.select("sales")

        filters = []
        if product_id:
            filters.append(f"product_id = {product_id}")
        if employee_id:
            filters.append(f"employee_id = {employee_id}")
        if visitor_id:
            filters.append(f"visitor_id = {visitor_id}")

        if filters:
            query = query.where(" AND ".join(filters))

        result = query.execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@sales_bp.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    try:
        result = qb.select("sales").where(f"id={id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

