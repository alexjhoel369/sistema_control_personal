from flask import render_template

# Vista para listar todas las licencia_aprobadaes
# En views.py
def list(licencias):
    return render_template('admin/licencias_aprobadas/index.html', licencias=licencias)

def create(empleados, tipos_licencia):
    return render_template('admin/licencias_aprobadas/create.html', empleados=empleados, tipo_licencias=tipos_licencia)

def edit(licencia, empleados, tipo_licencias):
    return render_template('admin/licencias_aprobadas/edit.html', licencia=licencia, empleados=empleados, tipo_licencias=tipo_licencias)

#------director


def director_list(licencias_aprobadas):
    return render_template("director/licencia_aprobada/index.html", licencias_aprobadas=licencias_aprobadas)

def director_create(empleados, tipo_licencias):
    return render_template("director/licencia_aprobada/create.html", empleados=empleados, tipo_licencias=tipo_licencias)

def director_edit(licencia_aprobada, empleados, tipo_licencias):
    return render_template("director/licencias_aprobadas/edit.html", licencia_aprobada=licencia_aprobada, empleados=empleados, tipo_licencias=tipo_licencias)
#-------------------------------

def personal_list(licencias_aprobadas):
    return render_template("personal/licencia_aprobada/index.html", licencias_aprobadas=licencias_aprobadas)