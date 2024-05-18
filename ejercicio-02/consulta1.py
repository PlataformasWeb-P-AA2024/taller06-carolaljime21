# consulta_america.py
from genera_base import Pais
from sqlalchemy.orm import sessionmaker
from genera_base import engine
Session = sessionmaker(bind=engine)
from sqlalchemy import and_, or_ # se importa el operador and

session = Session()
paises_america = session.query(Pais).filter(or_(Pais.continente == "NA", Pais.continente == "SA")).all()
for pais in paises_america:
    print(pais.nombrePais)
session.close()
