from flask import request, redirect, url_for, Blueprint, session
from models.permiso_model import Permiso
from models.empleado_model import Empleado
from views import permiso_view
from datetime import date, datetime

permiso_bp = Blueprint('permiso', __name__, url_prefix='/permisos')
permiso_director_bp = Blueprint('permiso_director', __name__, url_prefix='/director/permisos')
permiso_personal_bp = Blueprint('permiso_personal', __name__, url_prefix='/personal/permisos')

# ---------------------- ADMIN ----------------------

@permiso_bp.route('/')
def index():
    permisos = Permiso.get_all()
    return permiso_view.list(permisos)

@permiso_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        motivo = request.form['motivo']
        estado = request.form.get('estado')
        empleado_id = int(request.form['empleado_id'])

        permiso = Permiso(fecha_solicitud, fecha_inicio, fecha_fin, motivo, estado, empleado_id)
        permiso.save()
        return redirect(url_for('permiso.index'))

    empleados = Empleado.query.all()
    fecha_actual = date.today().isoformat()
    return permiso_view.create(empleados=empleados, fecha_actual=fecha_actual)

@permiso_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    permiso = Permiso.get_by_id(id)
    if not permiso:
        return "Permiso no encontrado", 404

    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        permiso.update(
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=request.form['motivo'],
            estado=request.form.get('estado'),
            empleado_id=int(request.form['empleado_id'])
        )
        return redirect(url_for('permiso.index'))

    empleados = Empleado.query.all()
    return permiso_view.edit(permiso=permiso, empleados=empleados)

@permiso_bp.route('/delete/<int:id>')
def delete(id):
    permiso = Permiso.get_by_id(id)
    if permiso:
        permiso.delete()
    return redirect(url_for('permiso.index'))

# ---------------------- DIRECTOR ----------------------

@permiso_director_bp.route('/')
def index_director():
    permisos = Permiso.get_all()
    return permiso_view.director_list(permisos)

@permiso_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        permiso = Permiso(
            fecha_solicitud,
            fecha_inicio,
            fecha_fin,
            request.form['motivo'],
            request.form.get('estado'),
            int(request.form['empleado_id'])
        )
        permiso.save()
        return redirect(url_for('permiso_director.index_director'))

    empleados = Empleado.query.all()
    fecha_actual = date.today().isoformat()
    return permiso_view.director_create(empleados=empleados, fecha_actual=fecha_actual)

@permiso_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    permiso = Permiso.get_by_id(id)
    if not permiso:
        return "Permiso no encontrado", 404

    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        permiso.update(
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=request.form['motivo'],
            estado=request.form.get('estado'),
            empleado_id=int(request.form['empleado_id'])
        )
        return redirect(url_for('permiso_director.index_director'))

    empleados = Empleado.query.all()
    return permiso_view.director_edit(permiso=permiso, empleados=empleados)

# ---------------------- PERSONAL ----------------------

@permiso_personal_bp.route('/')
def index_personal():
    empleado_id = session.get('empleado_id')
    permisos = Permiso.query.filter_by(empleado_id=empleado_id).all()
    return permiso_view.personal_list(permisos)

@permiso_personal_bp.route('/create', methods=['GET', 'POST'])
def create_personal():
    empleado_id = session.get('empleado_id')
    if request.method == 'POST':
        fecha_solicitud = date.today()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        motivo = request.form['motivo']

        permiso = Permiso(
            fecha_solicitud,
            fecha_inicio,
            fecha_fin,
            motivo,
            estado='pendiente',
            empleado_id=empleado_id
        )
        permiso.save()
        return redirect(url_for('permiso_personal.index_personal'))

    fecha_actual = date.today().isoformat()
    return permiso_view.personal_create(fecha_actual=fecha_actual)

