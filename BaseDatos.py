import pymongo

class BaseDatos():

    def __init__(self):
        self._conexion = None

    def set_conexion(self, conexion):
        if(conexion == None):
            try:
                self._conexion = pymongo.MongoClient("mongodb://localhost:27017/")
            except:
                self._conexion = None
        else:
            self._conexion = conexion

    def get_conexion(self):
        return self._conexion

    def definir_raiz_agricultores(self, conexion):
        database = conexion.recomendacion_cultivos
        coleccion = database.agricultores
        return database, coleccion

    def definir_raiz_administradores(self, conexion):
        database = conexion.recomendacion_cultivos
        coleccion = database.administradores
        return database, coleccion

    def definir_raiz_cultivos(self, conexion):
        database = conexion.recomendacion_cultivos
        coleccion = database.cultivos
        return database, coleccion

    def definir_raiz_reglas(self, conexion):
        database = conexion.recomendacion_cultivos
        coleccion = database.reglas
        return database, coleccion
