class Crud:


    def obtenerPasswordUsuario(self, usuario, raiz):
        resultado = raiz.find_one({"documento": usuario})
        if resultado is None:
            estado = [False, None]
        else:
            estado = [True, resultado["password"]]
        return estado

    def comprobarPassword(self, estado, password):
        estadoCredenciales = False
        if estado[0]:
            if password == estado[1]:
                estadoCredenciales = True
            else:
                estadoCredenciales = False
        else:
            estadoCredenciales = False
        return estadoCredenciales

    def obtenerPasswordAdmin(self, usuario, raiz):
        resultado = raiz.find_one({"documento": usuario})
        if resultado is None:
            estado = [False, None]
        else:
            estado = [True, resultado["password"]]
        return estado

    def comprobarPasswordAdmin(self, estado, password):
        estadoCredenciales = False
        if estado[0]:
            if password == estado[1]:
                estadoCredenciales = True
            else:
                estadoCredenciales = False
        else:
            estadoCredenciales = False
        return estadoCredenciales

    def traerFincasUsuario(self, usuario, raiz):
        agricultor = raiz.find_one({"documento": usuario})
        fincas = agricultor["fincas"]
        return fincas

    def traerReglas(self, raiz):
        reglasLista = []
        cursorReglas = raiz.find()
        for i in cursorReglas:
            reglasLista.append(i["regla"])
        return reglasLista

    def traerCultivos(self, raiz):
        cultivosLista = []
        cursorCultivos = raiz.find()
        for i in cursorCultivos:
            cultivosLista.append(i)
        return cultivosLista

    def traerUnaFinca(self, usuario, raiz, nombre):
        fincas = self.traerFincasUsuario(usuario, raiz)
        for i in fincas:
            if i["nombre"] == nombre:
                return i

    def traerDatosUsuario(self, usuario, raiz):
        agricultor = raiz.find_one({"documento": usuario})
        nombre = agricultor["nombre"]
        return nombre

    def insertarFinca(self, usuario, raiz, fincaAdicionar):
        fincas = self.traerFincasUsuario(usuario, raiz)
        fincas.append({"id":3, "nombre": fincaAdicionar["nombre"], "zona": fincaAdicionar["zona"], "luminosidad": int(fincaAdicionar["luminosidad"]), "topografia": float(fincaAdicionar["topografia"]), "temperatura": float(fincaAdicionar["temperatura"]), "altura": int(fincaAdicionar["altura"]), "humedad": float(fincaAdicionar["humedad"]), "ph": float(fincaAdicionar["ph"]), "departamento": fincaAdicionar["departamento"], "region": fincaAdicionar["region"]})
        myquery = {"documento": usuario}
        newvalues = {"$set": {"fincas": fincas}}
        try:
            raiz.update_one(myquery, newvalues)
            estado = True
        except:
            estado = False
        return estado

    def tomarID(self, raiz):
        cursorCultivos = raiz.find()
        return cursorCultivos.count()

    def insertarCultivo(self, raiz, cultivoAdicionar):
        cultivos = {}
        id = self.tomarID(raiz) + 1
        cultivos = {"id": id, "nombre": cultivoAdicionar["cultivo"], "tipo": cultivoAdicionar["tipo"], "luminosidad_min": int(cultivoAdicionar["lumMin"]), "luminosidad_max": int(cultivoAdicionar["lumMax"]), "angulo_min": float(cultivoAdicionar["topMin"]), "angulo_max": float(cultivoAdicionar["topMax"]), "temperatura_min": float(cultivoAdicionar["tempMin"]), "temperatura_max": float(cultivoAdicionar["tempMax"]), "altura_min": int(cultivoAdicionar["alturaMin"]), "altura_max": int(cultivoAdicionar["alturaMax"]), "humedad_min": float(cultivoAdicionar["humMin"]), "humedad_max": float(cultivoAdicionar["humMax"]), "acidez_min": float(cultivoAdicionar["phMin"]), "acidez_max": float(cultivoAdicionar["phMax"])}
        try:
            raiz.insert_one(cultivos)
            estado = True
        except:
            estado = False
        return estado, cultivos

    def insertarRegla(self, raiz, regla):
        id = self.tomarID(raiz) + 1
        try:
            raiz.insert_one({"id": id, "regla": regla})
            estado = True
        except:
            estado = False
        return estado





