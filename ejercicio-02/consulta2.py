# consulta_america.py
from genera_base import Pais
from sqlalchemy.orm import sessionmaker
from genera_base import engine
Session = sessionmaker(bind=engine)
from sqlalchemy import and_, or_ # se importa el operador and

session = Session()
paises_asia = session.query(Pais).filter(Pais.continente == "AS").order_by(Pais.dial).all()
for pais in paises_asia:
    print(pais.nombrePais, pais.dial)
session.close()
