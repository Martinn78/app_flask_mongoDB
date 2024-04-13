from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://martin:yotengoelpoder_78@cluster0.vflobsv.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAfile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db