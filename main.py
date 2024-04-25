from fastapi import FastAPI, HTTPException #FastAPI es para crear aplicacion web
from db.db import client
from controller.usuarioCrud import router as usuarios_router #alias para router


app = FastAPI()
app.include_router(usuarios_router, tags=["usuarios"], prefix="/usuarios") #todas las rutas que definamos tendran "/usuarios" por default gracias al router

@app.on_event("shutdown") #asegura que la conexión se cierre correctamente cuando la aplicación se detenga
def shutdown_db_client():
    client.close()



