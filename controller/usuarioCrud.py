from typing import List #importar para hacer listas

from fastapi import HTTPException, APIRouter #desarrollar apis rest, HTTPException es para las solitudes HTPP (manejar errores), APIRouter es para las rutas url (agrupar y definir)
from db.db import collection #importamos la base de datos
from modelo.usuario import Usuario #importamos la clase Usuario

router = APIRouter()

@router.post("/", response_description="Crear un nuevo usuario", response_model=Usuario) #response_model = el tipo de dato que vamos a devolver como respuesta
#como la base de datos es asincrona se pone await antes de la collection
async def create_usuario(usuario: Usuario): #como parametro es un usuario que se espera sea un objeto de tipo Usuario
    existing_user = await collection.find_one({"email": usuario.email}) #verificamos que no exista usuario por su email (por diccionario)
    if existing_user != None:
        raise HTTPException(status_code=404, detail="Email ya existe")
    result = await collection.insert_one(usuario.dict()) #si no se encuentra el email se crea el usuario y transformamos el objeto usuario a un json con el diccionario (el diccionario es como un json)
    usuario._id = str(result.inserted_id) #insert_one regresa un objeto InsertOneResult y dentro de este hay info sobre la operacion de insercion, entre esta info esta el id (inserted_id para recuperarlo) y lo casteamos a un str porque es un obj
    #se asigna _id al usuario
    #la comun nomenglatura de mongo es usar _ para el id
    return usuario

@router.get("/", response_description="Listar usuarios", response_model=List[Usuario])
async def read_usuarios():
    #creamos una lista de usuarios
    usuarios = await collection.find().to_list(100)
    for usuario in usuarios:
        usuario["_id"] = str(usuario["_id"]) #convierte el id a cada de texto
        print(usuario)
    return usuarios

@router.get("/{email}", response_model=Usuario) #esta ruta requiere un parametro llamado email
async def find_usuario_by_email(email: str):
    usuario = await collection.find_one({"email": email}) #busca el email del parametro
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.put("/{email}", response_model=Usuario)
async def uptade_usuario(email: str, usuario: Usuario):
    uptaded_usuario = await collection.find_one_and_update({"email": email}, {"$set": usuario.dict()}) #busca el email y actualiza los datos
    if uptaded_usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/{email}", response_model=Usuario)
async def delete_usuario(email: str):
    deleted_usuario = await collection.find_one_and_delete({"email": email})
    if deleted_usuario:
        return deleted_usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")