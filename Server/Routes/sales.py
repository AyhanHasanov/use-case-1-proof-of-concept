from flask import Response, Blueprint
import QueryBuilder

sales_bp = Blueprint("sales", __name__)
qb = QueryBuilder.QueryBuilder()

@sales_bp.route("/sales", methods=["GET"])
def get_all_sales():
    result = qb.select("sales").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@sales_bp.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    result = qb.select("sales").where(f"id={id}").execute()
    if not result:
        return Response(status=404)
    else:
        return result

