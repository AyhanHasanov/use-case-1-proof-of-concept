#Flask API
#Task 2

from flask import Flask

def create_app():
    app = Flask(__name__)
    from Routes.attractions import attractions_bp
    from Routes.employees import employees_bp
    from Routes.events import events_bp
    from Routes.sales import sales_bp
    from Routes.tickets import tickets_bp
    from Routes.transactions import transactions_bp
    from Routes.visitors import visitors_bp

    app.register_blueprint(attractions_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(visitors_bp)
    return app


app = Flask(__name__)

#--__name__ -> contains current's file name
# END POINT -> url address with a function attached to it
#localhost is the loopback ip of the machine -> 127.0.0.1:port
#routes/endpoints; to access localhost:5000/nameoffunc ->
# 127.0.0.1:5000/hello returns 'Hello, world'

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)

