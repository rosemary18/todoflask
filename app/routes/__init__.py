from app.routes.todo_routes import todo_routes

def register_blueprints(app):
    app.register_blueprint(todo_routes)