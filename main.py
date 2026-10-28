from fastapi import FastAPI #importa la clase que permite crear nuestra API

app = FastAPI() #instancia de la aplicacion

@app.get("/")  #define un endpoint que  responde a las peticiones HTTP GET en la ruta /
def read_rot(): #ejecutara cuando alguien visite esa ruta
    return {"message": "Welcome to ProductHub API"} #FastAPI lo convierte automaticamente a JSON



