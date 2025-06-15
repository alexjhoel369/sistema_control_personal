from flask import Blueprint, session, flash, redirect, url_for, request
from views import personal_view, solicitud_licencia_view
from views import licencia_aprobada_view, comunicado_view, historial_view
from controllers.auth_controller import login_required
from models.usuario_model import Usuario
from models.empleado_model import Empleado
from models.solicitud_licencia_model import SolicitudLicencia
from models.licencia_aprobada_model import LicenciaAprobada
from models.historial_model import Historial
from models.comunicado_model import Comunicado
from models.tipo_licencia_model import TipoLicencia

from datetime import datetime, date

personal_bp = Blueprint("personal", __name__, url_prefix="/personal")


# Middleware: acceso solo para el rol "personal"
@personal_bp.before_request
@login_required
def verificar_acceso():
    if session.get("user_role") != 3:  # 3: Personal
        flash("Acceso denegado. Solo personal autorizado.", "danger")
        return redirect(url_for("auth.login"))


# Dashboard principal
@personal_bp.route("/")
def dashboard():
    return personal_view.dashboard()


# Ver perfil personal
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


# Marcar asistencia
@personal_bp.route("/asistencia/marcar", methods=["GET", "POST"])
def marcar_asistencia():
    return personal_view.marcar_asistencia()


# Ver historial de asistencias
@personal_bp.route("/asistencia/historial")
def asistencia():
    return personal_view.ver_historial_asistencia()


# Ver solicitudes de licencia personales
@personal_bp.route("/solicitud_licencias/", methods=["GET"])
def ver_solicitudes_licencia():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    solicitudes = SolicitudLicencia.query.filter_by(empleado_id=empleado_id).order_by(SolicitudLicencia.fecha_solicitud.desc()).all()

    return solicitud_licencia_view.personal_list(solicitudes)


# Crear nueva solicitud de licencia (formulario)
@personal_bp.route("/solicitud_licencias/nuevo/", methods=["GET", "POST"])
def crear_solicitud_licencia():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)
    if not empleado:
        flash("Empleado no encontrado.", "warning")
        return redirect(url_for("personal.ver_solicitudes_licencia"))

    if request.method == "POST":
        fecha_solicitud_str = request.form.get("fecha_solicitud")
        fecha_inicio_str = request.form.get("fecha_inicio")
        fecha_fin_str = request.form.get("fecha_fin")
        motivo = request.form.get("motivo")
        tipo_id = request.form.get("tipo_id")

        fecha_solicitud = datetime.strptime(fecha_solicitud_str, "%Y-%m-%d").date()
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()

        nueva_solicitud = SolicitudLicencia(
            empleado_id=empleado.id,
            tipo_licencia_id=tipo_id,
            fecha_solicitud=fecha_solicitud,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            motivo=motivo,
            estado="pendiente"
        )
        nueva_solicitud.save()
        flash("Solicitud de licencia enviada correctamente.", "success")
        return redirect(url_for("personal.ver_solicitudes_licencia"))

    tipos = TipoLicencia.get_all()
    fecha_actual = date.today().strftime('%Y-%m-%d')
    return solicitud_licencia_view.personal_create(tipos, fecha_actual)


# Ver licencias aprobadas
@personal_bp.route("/licencias_aprobadas/")
def licencias_aprobadas():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    asignaciones = LicenciaAprobada.query.filter_by(empleado_id=empleado_id).all()

    return licencia_aprobada_view.personal_list(asignaciones)


# Ver comunicados
@personal_bp.route("/comunicados/", methods=["GET"])
def comunicados():
    comunicados = Comunicado.get_all()
    return comunicado_view.personal_list(comunicados)


# Ver historial laboral
@personal_bp.route("/historial", methods=["GET"])
def historial():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    historiales = Historial.get_by_empleado_id(empleado_id)

    return historial_view.personal_list(historiales)
