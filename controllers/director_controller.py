from flask import Blueprint, redirect, url_for, session, flash
from views.director_view import render_dashboard
from .auth_controller import login_required

# Crear Blueprint para el director
director_bp = Blueprint("director", __name__, url_prefix="/director")

@director_bp.before_request
@login_required
def verificar_acceso():
    # Verificar si el usuario es director (rol_id == 1)
    if session.get("user_role") != 2:
        flash("Acceso denegado. Debes ser directoristrador para acceder.", "danger")
        return redirect(url_for("auth.login"))

# Ruta principal del dashboard
@director_bp.route("/")
def dashboard():
    return render_dashboard()

@director_bp.route("/comunicados/")
def comunicados():
    return redirect(url_for("comunicado.index"))

@director_bp.route("/licencias_aprobadas/")
def licencias_aprobadas():
    return redirect(url_for("licencia_aprobada.index"))

@director_bp.route("/historiales/")
def historiales():
    return redirect(url_for("historial.index"))

@director_bp.route("/empleados/")
def empleados():
    return redirect(url_for("empleado.index"))

@director_bp.route("/solicitud_licencias/")
def permisos():
    return redirect(url_for("solicitud_licencia_director.index_director"))
