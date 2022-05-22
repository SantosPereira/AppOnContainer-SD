from datetime import datetime
from flask import Flask, render_template, request
from settings import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://dev:1234@banco/prod'

db = SQLAlchemy(app)

class Registro(db.Model):
    __tablename__ = 'registro'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(12), unique=True)
    hora_entrada = db.Column(db.DateTime)
    hora_saida = db.Column(db.DateTime, default=datetime.now)
    valor_pago = db.Column(db.Integer)
    recorrencia = db.Column(db.Integer)

    def __init__(self, placa, hora_entrada, hora_saida, valor_pago, recorrencia):
        self.placa = placa
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.valor_pago = valor_pago
        self.recorrencia = recorrencia

db.create_all()

@app.route("/")
def listar():
    registros = Registro.query.all()
    return render_template("index.html", registros=registros)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    placa = request.form.get('placa')
    hora_entrada = request.form.get('hora_entrada')
    hora_saida = datetime.now()
    valor_pago = request.form.get('valor_pago')
    recorrencia = 1
    r = Registro(placa, hora_entrada, hora_saida, valor_pago, recorrencia)
    db.session.add(r)
    db.session.commit()
    return render_template("index.html", registro=r)

@app.route("/alterar/<int:id>", methods=["GET"])
def alterar(id):
    r = Registro.query.filter_by(id=id).first()
    return render_template("alterarRegistro.html", registro=r)

@app.route("/alterar/<int:id>/salvar", methods=["POST"])
def salvar(id):
    r = Registro.query.filter_by(id=id).first()
    placa = request.form.get('placa')
    r.placa = placa
    db.session.add(r)
    db.session.commit()
    return render_template('index.html')

@app.route("/apagar/<int:id>")
def deletar(id):
    r = Registro.query.filter_by(id=id).first()
    db.session.delete(r)
    db.session.commit()
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
