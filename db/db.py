#diferentes formas de importar, cuando se pone import se esta trayendo solo esa parte del paquete

import certifi #seguridad para poder conectarnos
from motor.motor_asyncio import AsyncIOMotorClient #para interactuar con la base de datos de forma asincrona
import os #para leer variables de entorno (archivo .env)
from dotenv import load_dotenv #para leer el archivo .env

load_dotenv() #se llama a la funcion para leer el archivo .env

#crear cadena de conexion
MONGO_URL = os.environ.get("MONGO_DB")

#crear el cliente con AsyncIOMotorClient
#Este cliente representa una conexión al servidor de MongoDB y se utiliza para realizar operaciones en la base de datos
client = AsyncIOMotorClient(MONGO_URL, tlsCAFile=certifi.where()) #tlsCAFile=certifi.where() = asegura que la conexión entre el cliente y el servidor de MongoDB sea segura y confiable.

#obtener la base de datos y la coleccion con la que vamos a trabajar
database = client["ing_software"]
collection = database["usuarios"]