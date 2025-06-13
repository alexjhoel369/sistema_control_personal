from flask import request, redirect, url_for, Blueprint
from models.comunicado_model import Comunicado
from models.usuario_model import Usuario
from views import comunicado_view
from datetime import datetime

comunicado_bp = Blueprint('comunicado', __name__, url_prefix='/comunicados')
comunicado_director_bp = Blueprint('comunicado_director', __name__, url_prefix='/director/comunicados')


@comunicado_bp.route('/')
def index():
    comunicados = Comunicado.get_all()
    return comunicado_view.list(comunicados)

@comunicado_bp.route('/create', methods=['GET', 'POST'])
def create():
    from models.usuario_model import Usuario  
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        fecha_publicacion = Comunicado.convert_to_date(request.form.get('fecha_publicacion'))
        usuario_id = request.form['usuario_id']

        comunicado = Comunicado(titulo, contenido, fecha_publicacion, usuario_id)
        comunicado.save()
        return redirect(url_for('comunicado.index'))

    usuarios = Usuario.query.all()
    return comunicado_view.create(usuarios=usuarios)

@comunicado_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    from models.usuario_model import Usuario
    comunicado = Comunicado.get_by_id(id)
    if not comunicado:
        return "Comunicado no encontrado", 404

    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        fecha_publicacion = Comunicado.convert_to_date(request.form.get('fecha_publicacion'))
        usuario_id = request.form['usuario_id']

        comunicado.update(
            titulo=titulo,
            contenido=contenido,
            fecha_publicacion=fecha_publicacion,
            usuario_id=usuario_id
        )
        return redirect(url_for('comunicado.index'))

    usuarios = Usuario.query.all()
    return comunicado_view.edit(comunicado=comunicado, usuarios=usuarios)

@comunicado_bp.route('/delete/<int:id>')
def delete(id):
    comunicado = Comunicado.get_by_id(id)
    if comunicado:
        comunicado.delete()
    return redirect(url_for('comunicado.index'))

#----------------------

@comunicado_director_bp.route('/')
def index_director():
    comunicados = Comunicado.get_all()
    return comunicado_view.director_list(comunicados)

@comunicado_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        fecha_publicacion = Comunicado.convert_to_date(request.form.get('fecha_publicacion'))
        usuario_id = request.form['usuario_id']

        comunicado = Comunicado(titulo, contenido, fecha_publicacion, usuario_id)
        comunicado.save()
        return redirect(url_for('comunicado_director.index_director'))

    usuarios = Usuario.query.all()
    return comunicado_view.director_create(usuarios=usuarios)

@comunicado_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    comunicado = Comunicado.get_by_id(id)
    if not comunicado:
        return "Comunicado no encontrado", 404

    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        fecha_publicacion = Comunicado.convert_to_date(request.form.get('fecha_publicacion'))
        usuario_id = request.form['usuario_id']

        comunicado.update(
            titulo=titulo,
            contenido=contenido,
            fecha_publicacion=fecha_publicacion,
            usuario_id=usuario_id
        )
        return redirect(url_for('comunicado_director.index_director'))

    usuarios = Usuario.query.all()
    return comunicado_view.director_edit(comunicado=comunicado, usuarios=usuarios)
