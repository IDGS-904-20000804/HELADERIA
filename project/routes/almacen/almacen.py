from flask import Blueprint, render_template, request, redirect, url_for
from controllers.almacen.almacen_Controllers import obtener_almacen
from db.db import get_connection 
from flask_security import roles_required, login_required
import datetime
from models.login.ModeloLogin import ModeloLogin
from flask_login import login_required, current_user, UserMixin
import ast

almacen = Blueprint('almacen', __name__)


@almacen.route('/almacen', methods=["POST", "GET"])
@login_required
def almacenP():
    
    emp = obtener_almacen()
    emp1=sumar_cantidades(emp)
    user_id = current_user.id_usuario
    db = get_connection()
    datos = ModeloLogin.get_by_id(db, user_id)
    list = ast.literal_eval(datos.roles)
    return render_template('almacen.html', almacen=emp1, roles=list)

def sumar_cantidades(tuplas):
    diccionario = {}
    for tupla in tuplas:
        if tupla[1] in diccionario:
            diccionario[tupla[1]] += tupla[2]
        else:
            diccionario[tupla[1]] = tupla[2]

    resultado = []
    for nombre, cantidad in diccionario.items():
        unidad = ''
        for tupla in tuplas:
            if tupla[1] == nombre:
                unidad = tupla[3]
                break
        resultado.append((1, nombre, cantidad, unidad, datetime.datetime.now()))
    return resultado