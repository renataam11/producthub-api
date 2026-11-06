from fastapi import FastAPI, status #importa la clase que permite crear nuestra API
from models import Product

app = FastAPI() #instancia de la aplicacion
products = []
next_product_id = 1

@app.get("/")  #define un endpoint que  responde a las peticiones HTTP GET en la ruta /
def read_rot(): #ejecutara cuando alguien visite esa ruta
    return {"message": "Welcome to ProductHub API"} #FastAPI lo convierte automaticamente a JSON

@app.get("/health")
def health_check():
    return{"status": "healthy"}

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product:Product):
    global next_product_id

    new_product = {
        "id": next_product_id,
        **product.model_dump()
    }

    products.append(new_product)
    next_product_id += 1

    return new_product

@app.get("/products")
def get_products():
    return products





