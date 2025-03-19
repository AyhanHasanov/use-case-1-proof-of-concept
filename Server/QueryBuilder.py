from Routes import connection

class QueryBuilder:
    def __init__(self):
        self.query = ""
        self.is_select = False
        self.is_where_started = False

    def select(self, table, columns = "*"):
        if isinstance(columns, list):
            columns = ", ".join(columns)

        self.query = f"SELECT {columns} FROM {table}"
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
                col_val.append(f"{columns[x]} = {new_values[x]}")

            self.query += (", ".join(col_val))
            return self

        #expected one column
        self.query += f"{columns}={new_values}"
        return self

    def insert(self, table, columns, values):
        self.query = f"INSERT INTO {table} "

        if columns is not None:
            if isinstance(columns, list):
                self.query += f"({', '.join(columns)}) "

            if isinstance(columns, str):
                self.query += f"({columns}) "

        formatted_values = []

        for value in values:
            if isinstance(value, str):  #if string
                formatted_values.append(f"'{value}'")

            if isinstance(value, (int, float)):  #if number
                formatted_values.append(str(value))

        self.query += f"VALUES ({', '.join(formatted_values)})"
        return self

    def where(self, clause, compared_value = None):
        if compared_value is None or compared_value == "":
            self.is_where_started = False
            return self

        print("where is being run")
        if isinstance(compared_value, str):
            compared_value = f"'{compared_value}'"

        self.is_where_started = True
        self.query += f" WHERE {clause} {compared_value}"

        return self

    def and_where(self, clause, compared_value = None):
        self.query += self.__add_where_clauses("AND", clause, compared_value)
        return self

    def or_where(self, clause, compared_value = None):
        self.query += self.__add_where_clauses("OR", clause, compared_value)
        return self

    def print_query(self):
        print(self.query)
        return self

    def execute(self):
        print(self.query)
        try:
            res = connection.curs.execute(self.query)
            print("Query was executed successfully!")

            if self.is_select:
                column_names = []
                for desc in connection.curs.description:
                    column_names.append(desc[0])

                results = connection.curs.fetchall()
                output = []

                for row in results:
                    row_dict = {}
                    pairs = zip(column_names, row)
                    for col_name, value in pairs:
                        row_dict[col_name] = value
                    output.append(row_dict)

                print(output)
                return output

            return res

        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def __add_where_clauses(self, clause_type ,clause, compared_value = None):
        if compared_value is None or compared_value == "":
            return ""

        if isinstance(compared_value, str):
            compared_value = f"'{compared_value}'"

        # if there's no where started, start it
        if not self.is_where_started:
            self.is_where_started = True
            return f" WHERE {clause} {compared_value}"

        return f" {clause_type} {clause} {compared_value}"
