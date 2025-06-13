from flask import request, redirect, url_for, Blueprint, flash
from models.materia_asignada_model import Materia_asignada
from views import materia_asignada_view
from models.empleado_model import Empleado
from models.materia_model import Materia

materia_asignada_bp = Blueprint('materia_asignada', __name__, url_prefix='/materias_asignadas')
materia_asignada_director_bp = Blueprint('materia_asignada_director', __name__, url_prefix='/director/materias_asignadas')

# ---------- ADMIN ---------- #
@materia_asignada_bp.route('/')
def index():
    asignaciones = Materia_asignada.get_all()
    return materia_asignada_view.list(asignaciones)

@materia_asignada_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            empleado_id = request.form['empleado_id']
            materia_id = request.form['materia_id']
            gestion = request.form.get('gestion')

            asignacion = Materia_asignada(empleado_id, materia_id, gestion)
            asignacion.save()
            flash("Asignación creada correctamente.", "success")
            return redirect(url_for('materia_asignada.index'))
        except Exception as e:
            flash(f"Error al crear asignación: {str(e)}", "danger")

    empleados = Empleado.get_all()
    materias = Materia.get_all()
    return materia_asignada_view.create(empleados, materias)

@materia_asignada_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    asignacion = Materia_asignada.get_by_id(id)
    if not asignacion:
        return "Asignación no encontrada", 404

    if request.method == 'POST':
        try:
            empleado_id = request.form.get('empleado_id')
            materia_id = request.form.get('materia_id')
            gestion = request.form.get('gestion')

            asignacion.update(empleado_id=empleado_id, materia_id=materia_id, gestion=gestion)
            flash("Asignación actualizada correctamente.", "success")
            return redirect(url_for('materia_asignada.index'))
        except Exception as e:
            flash(f"Error al actualizar asignación: {str(e)}", "danger")

    empleados = Empleado.get_all()
    materias = Materia.get_all()
    return materia_asignada_view.edit(asignacion, empleados, materias)

@materia_asignada_bp.route('/delete/<int:id>')
def delete(id):
    asignacion = Materia_asignada.get_by_id(id)
    if asignacion:
        try:
            asignacion.delete()
            flash("Asignación eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar asignación: {str(e)}", "danger")
    else:
        flash("Asignación no encontrada.", "warning")
    return redirect(url_for('materia_asignada.index'))


# ---------- DIRECTOR ---------- #
@materia_asignada_director_bp.route('/')
def index_director():
    asignaciones = Materia_asignada.get_all()
    return materia_asignada_view.director_list(asignaciones)

@materia_asignada_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        try:
            empleado_id = request.form['empleado_id']
            materia_id = request.form['materia_id']
            gestion = request.form.get('gestion')

            asignacion = Materia_asignada(empleado_id, materia_id, gestion)
            asignacion.save()
            flash("Asignación creada correctamente.", "success")
            return redirect(url_for('materia_asignada_director.index_director'))
        except Exception as e:
            flash(f"Error al crear asignación: {str(e)}", "danger")

    empleados = Empleado.get_all()
    materias = Materia.get_all()
    return materia_asignada_view.director_create(empleados, materias)

@materia_asignada_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    asignacion = Materia_asignada.get_by_id(id)
    if not asignacion:
        return "Asignación no encontrada", 404

    if request.method == 'POST':
        try:
            empleado_id = request.form.get('empleado_id')
            materia_id = request.form.get('materia_id')
            gestion = request.form.get('gestion')

            asignacion.update(empleado_id=empleado_id, materia_id=materia_id, gestion=gestion)
            flash("Asignación actualizada correctamente.", "success")
            return redirect(url_for('materia_asignada_director.index_director'))
        except Exception as e:
            flash(f"Error al actualizar asignación: {str(e)}", "danger")

    empleados = Empleado.get_all()
    materias = Materia.get_all()
    return materia_asignada_view.director_edit(asignacion, empleados, materias)

@materia_asignada_director_bp.route('/delete/<int:id>')
def delete_director(id):
    asignacion = Materia_asignada.get_by_id(id)
    if asignacion:
        try:
            asignacion.delete()
            flash("Asignación eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar asignación: {str(e)}", "danger")
    else:
        flash("Asignación no encontrada.", "warning")
    return redirect(url_for('materia_asignada_director.index_director'))
