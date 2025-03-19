from flask import Response, Blueprint
from flask import request
from QueryBuilder import QueryBuilder

transactions_bp = Blueprint('transactions', __name__)
qb = QueryBuilder()

@transactions_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    try:
        transaction_type = request.args.get("type")
        sale_id = request.args.get("sale_id")
        ticket_id = request.args.get("ticket_id")
        payroll_id = request.args.get("payroll_id")
        maintenance_id = request.args.get("maintenance_id")

        result = (qb.select("transactions")
                  .where("type =", transaction_type)
                  .and_where("sale_id =", sale_id)
                  .and_where("ticket_id =", ticket_id)
                  .and_where("payroll_id =", payroll_id)
                  .and_where("maintenance_id =", maintenance_id)
                  .execute())
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)

@transactions_bp.route("/transactions/<int:id>", methods=["GET"])
def get_transaction_by_id(id):
    try:
        result = qb.select("transactions").where("id =", id).execute()
        if not result:
            return Response(status=404)

        return result
    except:
        return Response(status=400)
