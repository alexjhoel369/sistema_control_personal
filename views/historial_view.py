from flask import render_template

def list(historiales):
    return render_template('admin/historial/index.html', historiales=historiales)

def create(empleados, usuarios):
    return render_template('admin/historial/create.html', empleados=empleados, usuarios=usuarios)

def edit(historial, empleados, usuarios):
    return render_template('admin/historial/edit.html', historial=historial, empleados=empleados, usuarios=usuarios)

def imprimir(**kwargs):
    # kwargs incluye empleado, historial_laboral, usuarios, materias_asignadas, asistencias, permisos
    return render_template('admin/historial/imprimir.html', **kwargs)

#-----------------------------------------------------

def director_list(historiales):
    return render_template('director/historial/index.html', historiales=historiales)

def imprimir_director(**kwargs):
    return render_template('director/historial/imprimir.html', **kwargs)

#-----------------------------------------------------

def personal_list(historiales):
    return render_template("personal/historial/index.html", historiales=historiales)