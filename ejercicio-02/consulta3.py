# consulta_america.py
from genera_base import Pais
from sqlalchemy.orm import sessionmaker
from genera_base import engine
Session = sessionmaker(bind=engine)
from sqlalchemy import and_, or_ # se importa el operador and

session = Session()
paises = session.query(Pais).all()
for pais in paises:
    print("%s (%s)" % (pais.nombrePais, pais.lenguajes))
session.close()
