from flask import render_template
from src.models.registro import Registro

def listar():
    registros = Registro.query.all()
    return render_template("index.html", registros)

def cadastrar():
    pass

def alterar(id):
    Registro.query.filter_by(id=id).first()
    # Passar dados para o template aqui
    return render_template("alterarRegistro")

def salvar():
    pass

def deletar(id):
    Registro.apagar(Registro.query.filter_by(id=id).first())
    return "Apagado com sucesso"
