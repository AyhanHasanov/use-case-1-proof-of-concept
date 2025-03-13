from flask import Response, Blueprint
from Routes import connection
import QueryBuilder

transactions_bp = Blueprint('transactions', __name__)
qb = QueryBuilder.QueryBuilder()

@transactions_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    result = qb.select("transactions").execute()
    if not result:
        return Response(status=404)
    else:
        return result

@transactions_bp.route("/transactions/<int:id>", methods=["GET"])
def get_transaction_by_id(id):
    result = qb.select("transactions").where(f"id = {id}").execute()
    if not result:
        return Response(status=404)
    else:
        return result
