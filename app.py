from flask import Flask, render_template, request, redirect, send_file, session
import random
import os
from scraper_maps import scrape_google_maps
from scraper_amarillas import scrape_paginas_amarillas
from utils import cargar_datos_existentes, guardar_resultados_nuevos, actualizar_estado_contacto

app = Flask(__name__)
app.secret_key = "superclave"

@app.route("/", methods=["GET", "POST"])
def index():
    estados = ["Colorado", "Texas", "California", "Florida", "Nevada"]
    resultados = cargar_datos_existentes()

    if request.method == "POST":
        estado = request.form.get("estado")
        categoria = request.form.get("categoria") or "negocio latino"

        session['estado'] = estado
        session['categoria'] = categoria

        fuente = random.choice(["maps", "amarillas"])
        if fuente == "maps":
            nuevos = scrape_google_maps(estado, categoria)
        else:
            nuevos = scrape_paginas_amarillas(estado, categoria)

        for fila in nuevos:
            if len(fila) < 6:
                fila.append("Pendiente")

        guardar_resultados_nuevos(nuevos)
        resultados = cargar_datos_existentes()

    return render_template("index.html", resultados=resultados, estados=estados, cantidad=len(resultados))

@app.route("/buscar_mas")
def buscar_mas():
    estado = session.get("estado", "Colorado")
    categoria = session.get("categoria", "negocio latino")
    fuente = random.choice(["maps", "amarillas"])

    if fuente == "maps":
        nuevos = scrape_google_maps(estado, categoria)
    else:
        nuevos = scrape_paginas_amarillas(estado, categoria)

    for fila in nuevos:
        if len(fila) < 6:
            fila.append("Pendiente")

    guardar_resultados_nuevos(nuevos)
    return redirect("/")

@app.route("/marcar", methods=["POST"])
def marcar():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    estado_contacto = request.form.get("estado")
    actualizar_estado_contacto(nombre, telefono, estado_contacto)
    return redirect("/")

@app.route("/exportar")
def exportar():
    return send_file("data/resultados.csv", as_attachment=True)

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    app.run(debug=True)
