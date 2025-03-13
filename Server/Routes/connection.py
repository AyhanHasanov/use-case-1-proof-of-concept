import snowflake.connector
import os
from dotenv import load_dotenv

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

def get_all_json(entity):
    try:
        query = f"select * from {entity}"
        curs.execute(query)
        column_names = [desc[0] for desc in curs.description]
        results = curs.fetchall()
        json_results = [dict(zip(column_names, row)) for row in results]
        return json_results
    except:
      print("An exception occurred")

def get_by_id_json(entity, id):
    try:
        curs.execute(f"select * from {entity} where id = {id}")
        column_names = [desc[0] for desc in curs.description]
        results = curs.fetchall()
        json_results = [dict(zip(column_names, row)) for row in results]
        return json_results
    except:
      print("An exception occurred")

def insert_query(query):
    curs.execute(query)
    conn.commit()
