from flask import Response, Blueprint
from flask import request
import QueryBuilder

qb = QueryBuilder.QueryBuilder()
products_bp = Blueprint('products', __name__)


@products_bp.route("/products", methods=["GET"])
def get_all_products():
    try:
        category = request.args.get('category')
        query = qb.select("products")

        if category:
            query = query.where(f"category = \'{category}\'").execute()

        result = query.execute()

        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)
