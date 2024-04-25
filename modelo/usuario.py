from pydantic import BaseModel #sirve para validar datos

class Usuario(BaseModel): #la clase se hereda de BadeModel para que asi se pueda validar que los datos cumplan con los requerimientos establecidos
    #mongo genera automaticamente un objeto id
    nombre: str
    email: str #para poder mapear
    password: str