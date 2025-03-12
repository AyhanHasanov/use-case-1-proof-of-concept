def get_all_json(entity,curs):
    try:
        query = f"select * from {entity}"
        curs.execute(query)
        column_names = [desc[0] for desc in curs.description]
        results = curs.fetchall()
        json_results = [dict(zip(column_names, row)) for row in results]
        return json_results
    except:
      print("An exception occurred")

def get_by_id_json(entity, id, curs):
    try:
        curs.execute(f"select * from {entity} where id = {id}")
        column_names = [desc[0] for desc in curs.description]
        results = curs.fetchall()
        json_results = [dict(zip(column_names, row)) for row in results]
        return json_results
    except:
      print("An exception occurred")
