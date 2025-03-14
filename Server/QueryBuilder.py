from Routes import connection

class QueryBuilder:
    def __init__(self):
        self.query = ""
        self.is_select = False

    def select(self, table, columns="*"):
        if type(columns) == list:
            self.query = f"SELECT " + (", ".join(columns))
        else:
            self.query = f"SELECT {columns}"

        self.query = self.query + f" FROM {table}"
        self.is_select = True
        return self

    def delete(self, table):
        self.query = f"DELETE FROM {table}"
        return self

    def update(self, table, columns, new_values):
        self.query = f"UPDATE {table} SET "
        if type(columns) == list and type(new_values) == list and len(new_values) == len(columns):
            #arrays, with matching values to the columns?
            col_val = []
            for x in range(len(new_values)):
                col_val.append(f"{columns[x]}={new_values[x]}")
            self.query += (", ".join(col_val))
        else:
            #expected one column?
            self.query += f"{columns}={new_values}"
        return self

    def insert(self, table, columns, values):
        self.query = f"INSERT INTO {table} "

        if columns != "":
            if isinstance(columns, list):
                self.query += f"({', '.join(columns)}) "
            else:
                self.query += f"({columns}) "
        else:
            #no columns provided -> insert into table values(value1, value2, ...)
            pass

        formatted_values = []
        for value in values:
            if isinstance(value, str):  #if string
                formatted_values.append(f"'{value}'")
            else:  #if number
                formatted_values.append(str(value))

        self.query += f"VALUES ({', '.join(formatted_values)})"
        return self

    def where(self, clause):
        self.query = self.query + f" WHERE {clause}"
        return self

    def print_query(self):
        print(self.query)
        return self

    def execute(self):
        print(self.query)
        res = connection.curs.execute(self.query)
        print("Executed")
        if self.is_select:
            column_names = [desc[0] for desc in connection.curs.description]
            results = connection.curs.fetchall()
            json_results = [dict(zip(column_names, row)) for row in results]
            return json_results
        else:
            return res

