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
    from Routes.products import products_bp

    app.register_blueprint(attractions_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(visitors_bp)
    app.register_blueprint(products_bp)
    return app


app = Flask(__name__)

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)

