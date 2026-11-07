from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)


@task_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    tasks = Task.query.order_by(Task.id.asc()).all()
    return render_template('tasks.html', tasks=tasks)


@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title = request.form.get('title', '').strip()
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty.', 'danger')

    return redirect(url_for('tasks.view_tasks'))


@task_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)
    if task.status == 'Pending':
        task.status = 'Working'
    elif task.status == 'Working':
        task.status = 'Done'
    else:
        task.status = 'Pending'
    db.session.commit()

    return redirect(url_for('tasks.view_tasks'))


@task_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('tasks.view_tasks'))

