from flask import Blueprint, render_template, url_for, request, redirect

from app.models.todo_model import TodoModel
from app.models import db

todo_routes = Blueprint('todo_routes', __name__)

@todo_routes.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = TodoModel(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = TodoModel.query.order_by(TodoModel.date_created).all()
        return render_template('index.html', tasks=tasks)

@todo_routes.route('/delete/<int:id>')
def delete(id):
    task_to_delete = TodoModel.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@todo_routes.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = TodoModel.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)
