from flask import render_template

# Vista para listar todas las asignaciones
def list(asignaciones):
    return render_template('admin/materia_asignada/index.html', asignaciones=asignaciones)

# Vista para mostrar el formulario de creación
def create(empleados, materias):
    return render_template('admin/materia_asignada/create.html', empleados=empleados, materias=materias)

# Vista para mostrar el formulario de edición
def edit(asignacion, empleados, materias):
    return render_template('admin/materia_asignada/edit.html', asignacion=asignacion, empleados=empleados, materias=materias)

#------director


def director_list(asignaciones):
    return render_template("director/materia_asignada/index.html", asignaciones=asignaciones)

def director_create(empleados, materias):
    return render_template("director/materia_asignada/create.html", empleados=empleados, materias=materias)

def director_edit(asignacion, empleados, materias):
    return render_template("director/materia_asignada/edit.html", asignacion=asignacion, empleados=empleados, materias=materias)
#-------------------------------

def personal_list(asignaciones):
    return render_template("personal/materia_asignada/index.html", asignaciones=asignaciones)