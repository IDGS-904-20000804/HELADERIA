from flask import Blueprint, render_template, request, redirect, url_for
from db.db import get_connection
from flask_wtf.csrf import CSRFProtect
from models.materiaPrima.materiaPrima_Forms import MateriaPrima
from controllers.materiaPrima.materiaPrima_Controllers import obtener_materia_prima

# csrf = CSRFProtect()
materiaPrima = Blueprint('materiaPrima', __name__ )

@materiaPrima.route('/materiaPrima', methods=["POST", "GET"])
def materiaP():
     if request.method == 'POST':
        # Aquí puedes agregar la lógica para procesar los datos enviados en la solicitud POST
        create_form = MateriaPrima(request.form)
      #   id_unidadMedida= ''
      #   nombre = create_form.nombre.data
      #   unidadMedida = create_form.unidadMedida.data
        # De cualquier modo, y si todo fue bien, redireccionar
        return redirect(url_for('materiaPrima.materiaPrima'))
     else:
        create_form = MateriaPrima()
        mp = obtener_materia_prima()
        print(mp)
        return render_template('materiaPrima.html', form=create_form, materiaPrima=mp)