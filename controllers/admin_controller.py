from flask import Blueprint, redirect, url_for, session, flash
from views.admin_view import render_dashboard
from .auth_controller import login_required

# Crear Blueprint para el administrador
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

#@admin_bp.before_request
#@login_required
#def verificar_acceso():
    # Verificar si el usuario es administrador (rol_id == 1)
#    if session.get("user_role") != 1:
#        flash("Acceso denegado. Debes ser administrador para acceder.", "danger")
#        return redirect(url_for("auth.login"))

##. quita los # de aqui para poder ingresar al administrador.##
# Ruta principal del dashboard
@admin_bp.route("/")
def dashboard():
    return render_dashboard()

# Rutas para módulos específicos (redirigen a sus respectivos blueprints)
@admin_bp.route("/roles/")
def roles():
    return redirect(url_for("rol.index"))

@admin_bp.route("/usuarios/")
def usuarios():
    return redirect(url_for("usuario.index"))

@admin_bp.route("/cargos/")
def cargos():
    return redirect(url_for("cargo.index"))

@admin_bp.route("/solicitud_licencias/")
def permisos():
    return redirect(url_for("solicitud_licencia.index"))

@admin_bp.route("/asistencias/")
def asistencias():
    return redirect(url_for("asistencia.index"))

@admin_bp.route("/comunicados/")
def comunicados():
    return redirect(url_for("comunicado.index"))

@admin_bp.route("/tipo_licencia/")
def materias():
    return redirect(url_for("tipo_licencia.index"))

@admin_bp.route("/licencias_aprobadas/")
def materias_asignadas():
    return redirect(url_for("licencia_aprobada.index"))

@admin_bp.route("/historiales/")
def historiales():
    return redirect(url_for("historial.index"))

@admin_bp.route("/empleados/")
def empleados():
    return redirect(url_for("empleado.index"))