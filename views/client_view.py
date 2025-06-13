from flask import render_template

def render_index(template_name):
    """
    Esta función renderiza el índice o cualquier otra página de cliente.
    """
    return render_template(template_name)
