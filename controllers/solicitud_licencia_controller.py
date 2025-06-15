from flask import request, redirect, url_for, Blueprint, session, flash
from models.solicitud_licencia_model import SolicitudLicencia
from models.empleado_model import Empleado
from models.tipo_licencia_model import TipoLicencia
from views import solicitud_licencia_view
from datetime import date, datetime

solicitud_licencia_bp = Blueprint('solicitud_licencia', __name__, url_prefix='/solicitudes_licencia')
solicitud_licencia_director_bp = Blueprint('solicitud_licencia_director', __name__, url_prefix='/director/solicitudes_licencia')
solicitud_licencia_personal_bp = Blueprint('solicitud_licencia_personal', __name__, url_prefix='/personal/solicitudes_licencia')

# ---------------------- ADMIN ----------------------

@solicitud_licencia_bp.route('/')
def index():
    solicitudes = SolicitudLicencia.get_all()
    return solicitud_licencia_view.list(solicitudes)

@solicitud_licencia_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fecha_solicitud = date.today()  # Automáticamente hoy
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        motivo = request.form['motivo']
        estado = request.form.get('estado')
        empleado_id = int(request.form['empleado_id'])
        tipo_licencia_id = int(request.form['tipo_licencia_id'])

        solicitud = SolicitudLicencia(
            fecha_solicitud, fecha_inicio, fecha_fin, motivo, estado, empleado_id, tipo_licencia_id
        )
        solicitud.save()
        return redirect(url_for('solicitud_licencia.index'))

    empleados = Empleado.query.all()
    tipos = TipoLicencia.query.all()
    fecha_actual = date.today().isoformat()
    return solicitud_licencia_view.create(empleados=empleados, tipos=tipos, fecha_actual=fecha_actual)


@solicitud_licencia_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    solicitud = SolicitudLicencia.get_by_id(id)
    if not solicitud:
        return "Solicitud no encontrada", 404

    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        solicitud.update(
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=request.form['motivo'],
            estado=request.form.get('estado'),
            empleado_id=int(request.form['empleado_id']),
            tipo_licencia_id=int(request.form['tipo_licencia_id'])
        )
        return redirect(url_for('solicitud_licencia.index'))

    empleados = Empleado.query.all()
    tipos = TipoLicencia.query.all()
    return solicitud_licencia_view.edit(solicitud=solicitud, empleados=empleados, tipos=tipos)

@solicitud_licencia_bp.route('/delete/<int:id>')
def delete(id):
    solicitud = SolicitudLicencia.get_by_id(id)
    if solicitud:
        solicitud.delete()
    return redirect(url_for('solicitud_licencia.index'))

# ---------------------- DIRECTOR ----------------------

@solicitud_licencia_director_bp.route('/')
def index_director():
    solicitudes = SolicitudLicencia.get_all()

    # Agregar atributo temporal de días de permiso
    for solicitud in solicitudes:
        if solicitud.fecha_inicio and solicitud.fecha_fin:
            solicitud.dias_permiso = (solicitud.fecha_fin - solicitud.fecha_inicio).days + 1
        else:
            solicitud.dias_permiso = 0

    return solicitud_licencia_view.director_list(solicitudes)


@solicitud_licencia_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        solicitud = SolicitudLicencia(
            fecha_solicitud,
            fecha_inicio,
            fecha_fin,
            request.form['motivo'],
            request.form.get('estado'),
            int(request.form['empleado_id']),
            int(request.form['tipo_licencia_id'])
        )
        solicitud.save()
        return redirect(url_for('solicitud_licencia_director.index_director'))

    empleados = Empleado.query.all()
    tipos = TipoLicencia.query.all()
    fecha_actual = date.today().isoformat()
    return solicitud_licencia_view.director_create(empleados=empleados, tipos=tipos, fecha_actual=fecha_actual)

@solicitud_licencia_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    solicitud = SolicitudLicencia.get_by_id(id)
    if not solicitud:
        return "Solicitud no encontrada", 404

    if request.method == 'POST':
        fecha_solicitud = datetime.strptime(request.form['fecha_solicitud'], '%Y-%m-%d').date()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()

        solicitud.update(
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=request.form['motivo'],
            estado=request.form.get('estado'),
            empleado_id=int(request.form['empleado_id']),
            tipo_licencia_id=int(request.form['tipo_licencia_id'])
        )
        return redirect(url_for('solicitud_licencia_director.index_director'))

    empleados = Empleado.query.all()
    tipos = TipoLicencia.query.all()
    return solicitud_licencia_view.director_edit(solicitud=solicitud, empleados=empleados, tipos=tipos)

# ---------------------- PERSONAL ----------------------

@solicitud_licencia_personal_bp.route('/')
def index_personal():
    empleado_id = session.get('empleado_id')
    solicitudes = SolicitudLicencia.query.filter_by(empleado_id=empleado_id).all()
    return solicitud_licencia_view.personal_list(solicitudes)

@solicitud_licencia_personal_bp.route('/create', methods=['GET', 'POST'])
def create_personal():
    empleado_id = session.get('empleado_id')
    if request.method == 'POST':
        fecha_solicitud = date.today()
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        motivo = request.form['motivo']
        tipo_licencia_id = int(request.form['tipo_licencia_id'])

        solicitud = SolicitudLicencia(
            fecha_solicitud,
            fecha_inicio,
            fecha_fin,
            motivo,
            estado='pendiente',
            empleado_id=empleado_id,
            tipo_licencia_id=tipo_licencia_id
        )
        solicitud.save()
        return redirect(url_for('solicitud_licencia_personal.index_personal'))

    tipos = TipoLicencia.query.all()
    fecha_actual = date.today().isoformat()
    return solicitud_licencia_view.personal_create(tipos=tipos, fecha_actual=fecha_actual)

