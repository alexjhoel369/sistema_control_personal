from flask import render_template

def render_dashboard():
    """
    Renderiza el dashboard principal del administrador.
    """
    return render_template("admin/dashboard.html")
