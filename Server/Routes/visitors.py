from app import app
from flask import Response, Blueprint
from flask import request
from Routes import connection

visitors_bp = Blueprint('visitors', __name__)

@visitors_bp.route("/visitors", methods=["GET"])
def get_all_visitors():
    result = connection.get_all_json("visitors;")
    if not result:
        return Response(status=404)
    else:
        return result

@visitors_bp.route("/visitors/<int:id>", methods=["GET"])
def get_visitor_by_id(id):
    result = connection.get_by_id_json("visitors",id)
    if not result:
        return Response(status=404)
    else:
        return result


@visitors_bp.route("/visitors", methods=["POST"])
def create_visitor():
    try:
        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        query = f"insert into visitors(name, email, phone) values ('{name}', '{email}', '{phone}')"
        connection.insert_query(query)
        return Response(status=201)
    except:
        print("An exception occurred when creating visitor")
        return Response(status=500)

@visitors_bp.route("/visitors/<int:id>", methods=["PUT"])
def update_visitor_by_id(id):
    #find the entity first
    result = connection.get_by_id_json("visitors",id)
    if not result:
        return Response(status=404) #entity doesnt exist, cant be updated
    else:
        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        query = f"update visitors set name = '{name}', email = '{email}', phone = '{phone}' where id = {id}"
        connection.insert_query(query)
        return Response(status=200)

@visitors_bp.route("/visitors/<int:id>", methods=["DELETE"])
def delete_visitor_by_id(id):
    result = connection.get_by_id_json("visitors",id)
    if not result:
        return Response(status=404)
    else:
        query = f"delete from visitors where id = {id}"
        connection.insert_query(query)
        return Response(status=200)