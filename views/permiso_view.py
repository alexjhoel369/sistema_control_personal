from flask import render_template

def list(permisos):
    return render_template('admin/permisos/index.html', permisos=permisos)

def create(empleados, fecha_actual):
    return render_template('admin/permisos/create.html', empleados=empleados, fecha_actual=fecha_actual)

def edit(permiso, empleados):
    return render_template('admin/permisos/edit.html', permiso=permiso, empleados=empleados)

from flask import render_template

# Vista para lista
def director_list(permisos):
    return render_template('director/permisos/index.html', permisos=permisos)

# Vista para crear
def director_create(empleados, fecha_actual):
    return render_template('director/permisos/create.html', empleados=empleados, fecha_actual=fecha_actual)

# Vista para editar
def director_edit(permiso, empleados):
    return render_template('director/permisos/edit.html', permiso=permiso, empleados=empleados)


# ---------------------- PERSONAL ----------------------

def personal_list(permisos):
    return render_template('personal/permisos/index.html', permisos=permisos)

def personal_create(fecha_actual):
    return render_template('personal/permisos/create.html', fecha_actual=fecha_actual)