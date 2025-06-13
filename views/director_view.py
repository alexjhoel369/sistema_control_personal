from flask import render_template

def render_dashboard():
    """
    Renderiza el dashboard principal del director.
    """
    return render_template("director/dashboard.html")
