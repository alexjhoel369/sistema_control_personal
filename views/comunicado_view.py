from flask import render_template

def list(comunicados):
    return render_template('admin/comunicado/index.html', comunicados=comunicados)

def create(usuarios):
    return render_template('admin/comunicado/create.html', usuarios=usuarios)


def edit(comunicado, usuarios):
    return render_template('admin/comunicado/edit.html', comunicado=comunicado, usuarios = usuarios)


#----------

def director_list(comunicados):
    return render_template("director/comunicado/index.html", comunicados=comunicados)

def director_create(usuarios):
    return render_template("director/comunicado/create.html", usuarios=usuarios)

def director_edit(comunicado, usuarios):
    return render_template("director/comunicado/edit.html", comunicado=comunicado, usuarios=usuarios)

#-----------


def personal_list(comunicados):
    return render_template("personal/comunicado/index.html", comunicados=comunicados)
