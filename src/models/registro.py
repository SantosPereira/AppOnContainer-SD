from enum import unique
from sqlalchemy import Column, Integer, String, DateTime
from src.util.CursorBD import Base, db_session

class Registro(Base):
    __tablename__ = 'registro'
    id = Column(Integer, primary_key=True)
    placa = Column(String, unique=True)
    hora_entrada = Column(DateTime)
    hora_saida = Column(DateTime)
    valor_pago = Column(Integer)
    recorrencia = Column(Integer)

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()

    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()
