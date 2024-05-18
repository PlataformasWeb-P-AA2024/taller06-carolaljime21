from sqlalchemy.orm import sessionmaker
import requests
from genera_base import Pais
from genera_base import engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
response = requests.get(url)
data = response.json()

Session = sessionmaker(bind=engine)
session = Session()

for d in data:
    pais = Pais(
        nombrePais=d['CLDR display name'],
        capital=d['Capital'],
        continente=d['Continent'],
        dial=d['Dial'],
        geonameID=d['Geoname ID'],
        itu=d['ITU'],
        lenguajes=d['Languages'],
        esIndependiente=d['is_independent']
    )
    session.add(pais)

"""for d in data:
    print( "%s %s %s %s %d %s %s %s"      % (d["CLDR display name"], 
d["Capital"],
        d["Continent"],
        d["Dial"],
        d["Geoname ID"],
        d["ITU"],
        d["Languages"],
        d["is_independent"]))"""


session.commit()
session.close()