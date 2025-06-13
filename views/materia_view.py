from flask import render_template

#------ ADMIN
def list(materias):
    return render_template("admin/materias/index.html", materias=materias)

def create():
    return render_template("admin/materias/create.html")

def edit(materia):
    return render_template("admin/materias/edit.html", materia=materia)

#------ DIRECTOR
def director_list(materias):
    return render_template("director/materias/index.html", materias=materias)

def director_create():
    return render_template("director/materias/create.html")

def director_edit(materia):
    return render_template("director/materias/edit.html", materia=materia)
