#Flask API
#Task 2

import os
import snowflake.connector #USED TO ESTABLISH CONNECTION WITH SNOWFLAKE
import utill
from urllib import request
from dotenv import load_dotenv
from flask import Flask
from flask import Response
from flask import request


load_dotenv()
conn = snowflake.connector.connect(
    user=os.environ.get("SNOWFLAKE_USER"),
    password=os.environ.get("SNOWFLAKE_PASSWORD"),
    account=os.environ.get("SNOWFLAKE_ACCOUNT"),
    warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE"),
    database=os.environ.get("SNOWFLAKE_DATABASE"),
    schema=os.environ.get("SNOWFLAKE_SCHEMA"),
)

curs = conn.cursor()
app = Flask(__name__)
#--__name__ -> contains current's file name
# END POINT -> url address with a function attached to it
#localhost is the loopback ip of the machine -> 127.0.0.1:port
#routes/endpoints; to access localhost:5000/nameoffunc ->
# 127.0.0.1:5000/hello returns 'Hello, world'

@app.route("/attractions", methods=["GET"])
def get_all_attractions():
    result = utill.get_all_json("attractions", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/attractions/<int:id>", methods=["GET"])
def get_attraction_by_id(id):
    result = utill.get_by_id_json("attractions", id, curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/employees", methods=["GET"])
def get_all_employees():
    result = utill.get_all_json("employees", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    result = utill.get_by_id_json("employees", id, curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/sales", methods=["GET"])
def get_all_sales():
    result = utill.get_all_json("sales", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    result = utill.get_by_id_json("sales", id, curs)
    if not result:
        return Response(status=404)
    else:
        return result
@app.route("/tickets", methods=["GET"])
def get_all_tickets():
    result = utill.get_all_json("tickets", curs)
    if not result:
        return Response(status=404)
    else:
        return result
@app.route("/tickets/<int:id>", methods=["GET"])
def get_ticket_by_id(id):
    result = utill.get_by_id_json("tickets",id, curs)
    print(result)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/tickets", methods=["POST"])
def create_ticket():
    try:
        request_data = request.json
        price = request_data["PRICE"]
        promotion_id = request_data["PROMOTION_ID"]
        status = request_data["STATUS"]
        type_ = request_data["TYPE"]
        validity_end = request_data["VALIDITY_END"]
        validity_start = request_data["VALIDITY_START"]

        curs.execute(f"insert into tickets(price, promotion_id, status, type, validity_start, validity_end) "
                 f"values ({price}, {promotion_id}, '{status}', '{type_}', '{validity_start}', '{validity_end}')")
        conn.commit()

        return "Ticket successfully created and inserted in the database."
    except:
        print("An exception occurred when creating ticket")
        return Response(status=500)

@app.route("/events", methods=["GET"])
def get_all_events():
    result =  utill.get_all_json("special_events", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/events/<int:id>", methods=["GET"])
def get_event_by_id(id):
    result = utill.get_by_id_json("special_events",id, curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/visitors", methods=["GET"])
def get_all_visitors():
    result = utill.get_all_json("visitors;", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/visitors/<int:id>", methods=["GET"])
def get_visitor_by_id(id):
    result = utill.get_by_id_json("visitors",id, curs)
    if not result:
        return Response(status=404)
    else:
        return result

#not in the requirments
@app.route("/visitors", methods=["POST"])
def create_visitor():
    try:
        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        curs.execute(f"insert into visitors(name, email, phone) values ('{name}', '{email}', '{phone}')")
        conn.commit()
        return Response(status=201)
    except:
        print("An exception occurred when creating visitor")
        return Response(status=500)

@app.route("/visitors/<int:id>", methods=["PUT"])
def update_visitor_by_id(id):
    #find the entity first
    result = utill.get_by_id_json("visitors",id, curs)
    if not result:
        return Response(status=404) #entity doesnt exist, cant be updated
    else:
        request_data = request.json
        name = request_data["NAME"]
        email = request_data["EMAIL"]
        phone = request_data["PHONE"]
        curs.execute(f"update visitors set name = '{name}', email = '{email}', phone = '{phone}' where id = {id}")
        conn.commit()
        return Response(status=200)

@app.route("/visitors/<int:id>", methods=["DELETE"])
def delete_visitor_by_id(id):
    result = utill.get_by_id_json("visitors",id, curs)
    if not result:
        return Response(status=404)
    else:
        curs.execute(f"delete from visitors where id = {id}")
        conn.commit()
        return Response(status=200)

@app.route("/transactions", methods=["GET"])
def get_all_transactions():
    result = utill.get_all_json("transactions", curs)
    if not result:
        return Response(status=404)
    else:
        return result

@app.route("/transactions/<int:id>", methods=["GET"])
def get_transaction_by_id(id):
    result = utill.get_by_id_json("transactions",id, curs)
    if not result:
        return Response(status=404)
    else:
        return result

if __name__ == '__main__':
    app.run(debug = True)
