from flask import request, redirect, url_for, Blueprint, flash
from models.materia_model import Materia
from views import materia_view

materia_bp = Blueprint('materia', __name__, url_prefix='/materias')
materia_director_bp = Blueprint('materia_director', __name__, url_prefix='/director/materias')

#-------------------- ADMIN --------------------#
@materia_bp.route('/')
def index():
    materias = Materia.get_all()
    return materia_view.list(materias)

@materia_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            materia = Materia(nombre=nombre, descripcion=descripcion)
            materia.save()
            flash("Materia creada correctamente.", "success")
            return redirect(url_for('materia.index'))

        except Exception as e:
            flash(f"Error al crear materia: {str(e)}", "danger")

    return materia_view.create()

@materia_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    materia = Materia.get_by_id(id)
    if not materia:
        return "Materia no encontrada", 404

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            materia.update(nombre=nombre, descripcion=descripcion)
            flash("Materia actualizada correctamente.", "success")
            return redirect(url_for('materia.index'))

        except Exception as e:
            flash(f"Error al actualizar materia: {str(e)}", "danger")

    return materia_view.edit(materia)

@materia_bp.route('/delete/<int:id>')
def delete(id):
    materia = Materia.get_by_id(id)
    if materia:
        try:
            materia.delete()
            flash("Materia eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar materia: {str(e)}", "danger")
    else:
        flash("Materia no encontrada.", "warning")
    return redirect(url_for('materia.index'))

#-------------------- DIRECTOR --------------------#
@materia_director_bp.route('/')
def index_director():
    materias = Materia.get_all()
    return materia_view.director_list(materias)

@materia_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            materia = Materia(nombre=nombre, descripcion=descripcion)
            materia.save()
            flash("Materia creada correctamente.", "success")
            return redirect(url_for('materia_director.index_director'))

        except Exception as e:
            flash(f"Error al crear materia: {str(e)}", "danger")

    return materia_view.director_create()

@materia_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    materia = Materia.get_by_id(id)
    if not materia:
        return "Materia no encontrada", 404

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            materia.update(nombre=nombre, descripcion=descripcion)
            flash("Materia actualizada correctamente.", "success")
            return redirect(url_for('materia_director.index_director'))

        except Exception as e:
            flash(f"Error al actualizar materia: {str(e)}", "danger")

    return materia_view.director_edit(materia)

@materia_director_bp.route('/delete/<int:id>')
def delete_director(id):
    materia = Materia.get_by_id(id)
    if materia:
        try:
            materia.delete()
            flash("Materia eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar materia: {str(e)}", "danger")
    else:
        flash("Materia no encontrada.", "warning")
    return redirect(url_for('materia_director.index_director'))
