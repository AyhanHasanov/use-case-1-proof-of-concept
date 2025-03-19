from flask import Response, Blueprint
from flask import request
from QueryBuilder import QueryBuilder

sales_bp = Blueprint("sales", __name__)
qb = QueryBuilder()

@sales_bp.route("/sales", methods=["GET"])
def get_all_sales():
    try:
        product_id = request.args.get("product_id")
        employee_id = request.args.get("employee_id")
        visitor_id = request.args.get("visitor_id")

        result = (qb.select("sales")
                  .where("product_id =", product_id)
                  .and_where("employee_id =", employee_id)
                  .and_where("visitor_id =", visitor_id)
                  .execute())

        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@sales_bp.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    try:
        result = qb.select("sales").where("id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

