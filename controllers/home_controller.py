from flask import Blueprint, render_template

# Blueprint para las rutas del home
home_bp = Blueprint('home', __name__)

# Ruta principal - Página de presentación del sistema
@home_bp.route('/')
def index():
    return render_template('home/index.html')
