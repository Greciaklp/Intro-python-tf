# import the Flask class from the flask module
from fileinput import filename
from flask import Flask
from flask import request
from datetime import date, datetime

from modelos import Cuenta
from persona import Persona
from procesar_archivo import guardar_archivo, guardar_cuentas, procesar_archivo

app = Flask(__name__)




@app.route("/cuentas/")
def home():
    pass



@app.route("/subir-personas/", methods=["POST"])
def subir_personas():
    try:
        personas_csv = request.files["personas"]
        filename = guardar_archivo(personas_csv)
        cuentas = procesar_archivo(filename)
        guardar_cuentas(cuentas)
        return f"Archivo subido en {filename}"
    except KeyError:
        return "Request invalido, el archivo es obligatorio", 400


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
