from flask import request, redirect, url_for, Blueprint, flash
from models.licencia_aprobada_model import LicenciaAprobada
from models.empleado_model import Empleado
from models.tipo_licencia_model import TipoLicencia
from views import licencia_aprobada_view

licencia_aprobada_bp = Blueprint('licencia_aprobada', __name__, url_prefix='/licencias_aprobadas')
licencia_aprobada_director_bp = Blueprint('licencia_aprobada_director', __name__, url_prefix='/director/licencias_aprobadas')

# ---------- ADMIN ---------- #
@licencia_aprobada_bp.route('/')
def index():
    licencias = LicenciaAprobada.get_all()
    return licencia_aprobada_view.list(licencias)

@licencia_aprobada_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            empleado_id = request.form['empleado_id']
            tipo_licencia_id = request.form['tipo_licencia_id'] 
            gestion = request.form.get('gestion')

            licencia = LicenciaAprobada(empleado_id, tipo_licencia_id, gestion)
            licencia.save()
            flash("Licencia aprobada creada correctamente.", "success")
            return redirect(url_for('licencia_aprobada.index'))
        except Exception as e:
            flash(f"Error al crear licencia aprobada: {str(e)}", "danger")

    empleados = Empleado.get_all()
    tipos_licencia = TipoLicencia.get_all()
    return licencia_aprobada_view.create(empleados, tipos_licencia)

@licencia_aprobada_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if not licencia:
        return "Licencia aprobada no encontrada", 404

    if request.method == 'POST':
        try:
            empleado_id = request.form.get('empleado_id')
            tipo_licencia_id = request.form.get('tipo_licencia_id')
            gestion = request.form.get('gestion')

            licencia.update(empleado_id=empleado_id, tipo_licencia_id=tipo_licencia_id, gestion=gestion)
            flash("Licencia aprobada actualizada correctamente.", "success")
            return redirect(url_for('licencia_aprobada.index'))
        except Exception as e:
            flash(f"Error al actualizar licencia: {str(e)}", "danger")

    empleados = Empleado.get_all()
    tipos_licencia = TipoLicencia.get_all()
    return licencia_aprobada_view.edit(licencia, empleados, tipos_licencia)

@licencia_aprobada_bp.route('/delete/<int:id>')
def delete(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if licencia:
        try:
            licencia.delete()
            flash("Licencia eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar licencia: {str(e)}", "danger")
    else:
        flash("Licencia no encontrada.", "warning")
    return redirect(url_for('licencia_aprobada.index'))

# ---------- DIRECTOR ---------- #
@licencia_aprobada_director_bp.route('/')
def index_director():
    licencias = LicenciaAprobada.get_all()
    return licencia_aprobada_view.director_list(licencias)

@licencia_aprobada_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        try:
            empleado_id = request.form['empleado_id']
            tipo_licencia_id = request.form['tipo_licencia_id']
            gestion = request.form.get('gestion')

            licencia = LicenciaAprobada(empleado_id, tipo_licencia_id, gestion)
            licencia.save()
            flash("Licencia aprobada creada correctamente.", "success")
            return redirect(url_for('licencia_aprobada_director.index_director'))
        except Exception as e:
            flash(f"Error al crear licencia: {str(e)}", "danger")

    empleados = Empleado.get_all()
    tipos_licencia = TipoLicencia.get_all()
    return licencia_aprobada_view.director_create(empleados, tipos_licencia)

@licencia_aprobada_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if not licencia:
        return "Licencia aprobada no encontrada", 404

    if request.method == 'POST':
        try:
            empleado_id = request.form.get('empleado_id')
            tipo_licencia_id = request.form.get('tipo_licencia_id')
            gestion = request.form.get('gestion')

            licencia.update(empleado_id=empleado_id, tipo_licencia_id=tipo_licencia_id, gestion=gestion)
            flash("Licencia actualizada correctamente.", "success")
            return redirect(url_for('licencia_aprobada_director.index_director'))
        except Exception as e:
            flash(f"Error al actualizar licencia: {str(e)}", "danger")

    empleados = Empleado.get_all()
    tipos_licencia = TipoLicencia.get_all()
    return licencia_aprobada_view.director_edit(licencia, empleados, tipos_licencia)

@licencia_aprobada_director_bp.route('/delete/<int:id>')
def delete_director(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if licencia:
        try:
            licencia.delete()
            flash("Licencia eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar licencia: {str(e)}", "danger")
    else:
        flash("Licencia no encontrada.", "warning")
    return redirect(url_for('licencia_aprobada_director.index_director'))


