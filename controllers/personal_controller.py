from flask import Blueprint, session, flash, redirect, url_for, request
from views import personal_view, permiso_view  # 👈 asegúrate de que sea "permiso_view", no "permiso**s**_view"
from views import materia_asignada_view
from views import comunicado_view  # Vista que usaremos para mostrar los comunicados
from views import historial_view
from controllers.auth_controller import login_required
from models.usuario_model import Usuario
from models.empleado_model import Empleado
from models.permiso_model import Permiso
from models.materia_asignada_model import Materia_asignada
from models.historial_model import Historial
from models.comunicado_model import Comunicado 

from datetime import datetime, date

personal_bp = Blueprint("personal", __name__, url_prefix="/personal")

# Middleware: acceso solo para el rol "personal"
@personal_bp.before_request
@login_required
def verificar_acceso():
    if session.get("user_role") != 3:  # 3: Personal
        flash("Acceso denegado. Solo personal autorizado.", "danger")
        return redirect(url_for("auth.login"))

#  Dashboard principal
@personal_bp.route("/")
def dashboard():
    return personal_view.dashboard()

#  Ver perfil personal
@personal_bp.route("/mi_perfil/")
def mi_perfil():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)
    if not empleado:
        flash("Empleado no encontrado.", "warning")
        return redirect(url_for("personal.dashboard"))

    return personal_view.mi_perfil(empleado)

#  Marcar asistencia
@personal_bp.route("/asistencia/marcar", methods=["GET", "POST"])
def marcar_asistencia():
    return personal_view.marcar_asistencia()

#  Ver historial de asistencias
@personal_bp.route("/asistencia/historial")
def asistencia():
    return personal_view.ver_historial_asistencia()

#  Ver permisos personales (solo lectura)
@personal_bp.route("/permisos/", methods=["GET"])
def permisos():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id

    permisos = Permiso.query.filter_by(empleado_id=empleado_id).order_by(Permiso.fecha_solicitud.desc()).all()

    return permiso_view.personal_list(permisos)

#  Crear nuevo permiso (formulario)
@personal_bp.route("/permisos/nuevo/", methods=["GET", "POST"])
def crear_permiso():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)
    if not empleado:
        flash("Empleado no encontrado.", "warning")
        return redirect(url_for("personal.permisos"))

    if request.method == "POST":
        fecha_solicitud_str = request.form.get("fecha_solicitud") 
        fecha_inicio_str = request.form.get("fecha_inicio")
        fecha_fin_str = request.form.get("fecha_fin")
        motivo = request.form.get("motivo")
        # Convierte strings a objetos date:
        fecha_solicitud = datetime.strptime(fecha_solicitud_str, "%Y-%m-%d").date()
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()

        nuevo_permiso = Permiso(
            empleado_id=empleado.id,
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=motivo,
            estado="pendiente"
        )

        nuevo_permiso.save()
        flash("Permiso solicitado correctamente.", "success")
        return redirect(url_for("personal.permisos"))

    # Si es GET, mostrar el formulario
    fecha_actual = date.today().strftime('%Y-%m-%d')
    return permiso_view.personal_create(fecha_actual)


#  Ver materias asignadas
@personal_bp.route("/materias_asignadas/")
def materias_asignadas():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    asignaciones = Materia_asignada.query.filter_by(empleado_id=empleado_id).all()

    return materia_asignada_view.personal_list(asignaciones)


#  Ver comunicados
@personal_bp.route("/comunicados/", methods=["GET"])
def comunicados():
    comunicados = Comunicado.get_all()
    return comunicado_view.personal_list(comunicados)

#  Ver historial laboral
@personal_bp.route("/historial", methods=["GET"])
def historial():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    historiales = Historial.get_by_empleado_id(empleado_id)  # ✅ obtenemos lista

    return historial_view.personal_list(historiales)
