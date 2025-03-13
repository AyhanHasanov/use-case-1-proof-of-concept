from app import app
from flask import Response, Blueprint
from Routes import connection

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    result = connection.get_all_json("transactions")
    if not result:
        return Response(status=404)
    else:
        return result

@transactions_bp.route("/transactions/<int:id>", methods=["GET"])
def get_transaction_by_id(id):
    result = connection.get_by_id_json("transactions",id)
    if not result:
        return Response(status=404)
    else:
        return result
