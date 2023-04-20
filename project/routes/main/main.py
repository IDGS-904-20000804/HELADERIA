from flask import Blueprint, render_template, request, redirect, url_for,Request,flash
from flask_wtf.csrf import CSRFProtect
from db.db import get_connection 
from models.logi.ModeloLogin import ModeloLogin
from models.entities.User import User 
from flask_security import current_user

main = Blueprint('main', __name__ )


@main.route('/main')
def mains():
    user_id = current_user.id_usuario
    db = get_connection()
    print(user_id)
    id_usuario = user_id
    datos = ModeloLogin.get_by_id(db, id_usuario)
    roles = datos.roles  # asumiendo que roles es un arreglo de números
    role_labels = []
    for r in roles:
        role_labels += get_role_labels(r)
    return render_template('inicio.html', role_labels=role_labels)

def get_role_labels(role_num):
    if role_num == 1:
        return ['Administrador', 'Comprador', 'Gerente', 'Repartidor', 'Vendedor']
    elif role_num == 2:
        return ['Cliente']
    elif role_num == 3:
        return ['Vendedor']
    elif role_num == 4:
        return ['Repartidor']
    elif role_num == 5:
        return ['Comprador']
    elif role_num == 6:
        return ['Gerente']
    else:
        return ['Productor']
# def mains():
#     user_id = current_user.id_usuario
#     db = get_connection()
#     print(user_id)
#     id_usuario = user_id
#     datos = ModeloLogin.get_by_id(db, id_usuario)
#     roles = datos.roles  # asumiendo que roles es un arreglo de números
#     role_labels = [get_role_label(r) for r in roles]
#     return render_template('inicio.html', role_labels=role_labels)

# def get_role_label(role_num):
#     if role_num == 1:
#         return 'Administrador'
#     elif role_num == 2:
#         return 'Cliente'
#     elif role_num == 3:
#         return 'Vendedor'
#     elif role_num == 4:
#         return 'Repartidor'
#     elif role_num == 5:
#         return 'Comprador'
#     elif role_num == 6:
#         return 'Gerente'
#     else:
#         return 'Productor'
