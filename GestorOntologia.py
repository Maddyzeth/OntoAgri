import ModeloOntologico as onto

class GestorOntologia():

    def __init__(self):
        self._ontologia = ''

    def set_ontologia(self, ontologia):
        self._ontologia = ontologia

    def get_ontologia(self):
        return self._ontologia

    def crear_conceptos(self, finca):
        zona = onto.crear_zona(finca["zona"], finca["zona"])
        suelo = onto.crear_suelo()
        area = onto.crear_area(finca["nombre"], finca["nombre"])
        onto.asociar_area_zona(area, zona)
        onto.asociar_lum_zona(onto.crear_luminosity(finca["luminosidad"]), zona)
        onto.asociar_top_zona(onto.crear_topografia(finca["topografia"]), zona)
        onto.asociar_temp_zona(onto.crear_temperatura(finca["temperatura"]), zona)
        onto.asociar_alt_zona(onto.crear_altura(finca["altura"]), zona)
        onto.asociar_hum_zona(onto.crear_humedad(finca["humedad"]), zona)
        onto.asociar_zona_suelo(zona, suelo)
        onto.asociar_acidez_suelo(onto.crear_acidez(finca["ph"]), suelo)
        onto.iniciar_razonador()
        cultivos = onto.inferir_cultivo(area)
        return cultivos

    def armar_regla(self, datosCultivo, id):
        cultivo = 'crop' + str(id)
        regla = 'Temperature(?t), escalaTermicaMin(?t, ?temp), greaterThanOrEqual(?temp, ' + str(datosCultivo["temperatura_min"]) + '), lessThanOrEqual(?temp, ' + str(datosCultivo["temperatura_max"]) + '), Luminosity(?l), intensidadMin(?l, ?int), greaterThanOrEqual(?int, ' + str(datosCultivo["luminosidad_min"]) + '), lessThanOrEqual(?int, ' + str(datosCultivo["luminosidad_max"]) + '), Topography(?top), anguloMin (?top, ?esc), greaterThanOrEqual(?esc, ' + str(datosCultivo["angulo_min"]) + '), lessThanOrEqual(?esc, ' + str(datosCultivo["angulo_max"]) + '), Height(?h), distanciaMin(?h, ?dist), greaterThanOrEqual(?dist, ' + str(datosCultivo["altura_min"]) + '), lessThanOrEqual(?dist, ' + str(datosCultivo["altura_max"]) + '), Humidity(?hum), nivelMin(?hum, ?nivH), greaterThanOrEqual(?nivH, ' + str(datosCultivo["humedad_min"]) + '), lessThanOrEqual(?nivH, ' + str(datosCultivo["humedad_max"]) + '), Acidity(?ph), nivelMin(?ph, ?nivPh), greaterThanOrEqual(?nivPh, ' + str(datosCultivo["acidez_min"]) + '), lessThanOrEqual(?nivPh, ' + str(datosCultivo["acidez_max"]) + '), Zone(?z), ArableArea(?a), formsZone(?a, ?z), presents(?z, ?l), isRepresentedBy(?z, ?top), isLocatedAt(?z, ?h), hasHumidity(?z, ?hum), formsPartOf(?ph, ?land), Land(?land), hasLand(?z, ?land), hasTemperature(?z, ?t) -> grows(?a, ' + cultivo + ')'
        return regla


    def adicionar_reglas(self, regla):
        for i in regla:
            onto.crear_regla(i)
        onto.onto.rules()

    def adicionar_cultivos(self, cultivos):
        for i in cultivos:
            onto.crear_cultivo(i["nombre"], i["tipo"])


