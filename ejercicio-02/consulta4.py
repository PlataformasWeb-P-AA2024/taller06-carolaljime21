# consulta_america.py
from genera_base import Pais
from sqlalchemy.orm import sessionmaker
from genera_base import engine
Session = sessionmaker(bind=engine)
from sqlalchemy import and_, or_ # se importa el operador and

session = Session()
paises_europa = session.query(Pais).filter(Pais.continente == "EU").order_by(Pais.capital).all()
for pais in paises_europa:
    print("%s (%s)" % (pais.nombrePais, pais.capital))
session.close()
