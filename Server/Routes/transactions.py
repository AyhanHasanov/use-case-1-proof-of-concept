from flask import Response, Blueprint
from flask import request
import QueryBuilder

transactions_bp = Blueprint('transactions', __name__)
qb = QueryBuilder.QueryBuilder()

@transactions_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    try:
        type_ = request.args.get("type")
        sale_id = request.args.get("sale_id")
        ticket_id = request.args.get("ticket_id")
        payroll_id = request.args.get("payroll_id")
        maintanence_id = request.args.get("maintanence_id")

        query = qb.select("transactions")
        filters = []
        if type_:
            filters.append(f"type = '{type_}'")
        if sale_id:
            filters.append(f"sale_id = {sale_id}")
        if ticket_id:
            filters.append(f"ticket_id = {ticket_id}")
        if payroll_id:
            filters.append(f"payroll_id = {payroll_id}")
        if maintanence_id:
            filters.append(f"maintanence_id = {maintanence_id}")

        if filters:
            query = query.where(" AND ".join(filters))

        result = query.execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)

@transactions_bp.route("/transactions/<int:id>", methods=["GET"])
def get_transaction_by_id(id):
    try:
        result = qb.select("transactions").where(f"id = {id}").execute()
        if not result:
            return Response(status=404)
        else:
            return result
    except:
        return Response(status=400)
