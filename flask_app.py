from flask import Flask, redirect, render_template, request, url_for #Librerias de FLASK
from flask_sqlalchemy import SQLAlchemy #Libreria para modelar y mapear base de datos MYSQL
from sqlalchemy import text

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="letnetco_oit1",
    password="Oit_2019",
    hostname="64.37.61.194",
    databasename="letnetco_oit1",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299 #Cre que esto es el pool de conexión
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Datos(db.Model):#Aqui modelo la base de datos que se encuantra externa en el servidor que aloja los datos

    __tablename__ = "datos"

    id = db.Column(db.Integer, primary_key=True)# Campo de llave primaria
    chip = db.Column(db.String(4096))# Numero unico del dispositivo
    fecha = db.Column(db.String(4096))# fecha de inserción del registro
    dato = db.Column(db.String(4096))# contador de consumo


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", dato=Datos.query.filter_by(id = 5).all()) # Muestro el ultimo campo y lo envío a la plantilla

    comment = Comment(content=request.form["contents"])  # esto es remanente de un formulario que pienso usar despues.
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))