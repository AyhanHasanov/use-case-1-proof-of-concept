from flask import Response, Blueprint
from flask import request
from QueryBuilder import QueryBuilder

qb = QueryBuilder()
products_bp = Blueprint('products', __name__)

@products_bp.route("/products", methods=["GET"])
def get_all_products():
    try:
        category = request.args.get('category')
        result = qb.select("products").where(f"category =", category).execute()

        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)
