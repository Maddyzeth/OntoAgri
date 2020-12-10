from flask import Flask, flash, request, redirect, render_template, jsonify
import BaseDatos as bd
import GestorOntologia as go
import crud as crud

app = Flask(__name__)

conexion = None


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/loginagricultor', methods=['POST'])
def loginAgricultor():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    print(documento)
    password = data_dic["password"]
    print(password)
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    passwordsUsers = crudObj.obtenerPasswordUsuario(documento, agricultorRaiz)
    compPassword  = crudObj.comprobarPassword(passwordsUsers, password)
    print(compPassword)
    if compPassword:
        datosAgricultor = crudObj.traerDatosUsuario(documento, agricultorRaiz)
        return jsonify({'response': 'Success', 'documento': documento, 'nombre': datosAgricultor})
    else:
        return jsonify({'response': 'Error'})

@app.route('/agricultor', methods=['POST'])
def agricultor():
    data = request.form
    data_dictionary = data.copy()
    nombre_user = data_dictionary["nombre"]
    documento_user = data_dictionary["documento"]
    return render_template('agricultor.html', nombre=nombre_user, documento=documento_user)

@app.route('/loginadmin', methods=['POST'])
def loginAdmin():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    print(documento)
    password = data_dic["password"]
    print(password)
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, adminRaiz = basedatos.definir_raiz_administradores(conexion)
    passwordsUsers = crudObj.obtenerPasswordAdmin(documento, adminRaiz)
    compPassword  = crudObj.comprobarPasswordAdmin(passwordsUsers, password)
    print(compPassword)
    if compPassword:
        datosAdmin = crudObj.traerDatosUsuario(documento, adminRaiz)
        return jsonify({'response': 'Success', 'documento': documento, 'nombre': datosAdmin})
    else:
        return jsonify({'response': 'Error'})

@app.route('/administrador', methods=['POST'])
def administrador():
    data = request.form
    data_dictionary = data.copy()
    nombre_user = data_dictionary["nombre"]
    documento_user = data_dictionary["documento"]
    return render_template('administrador.html', nombre=nombre_user, documento=documento_user)


@app.route('/misfincas', methods=['POST'])
def misfincas():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    fincas = crudObj.traerFincasUsuario(documento, agricultorRaiz)
    listaFincas = []
    if fincas is None:
        return jsonify({'response': 'nofincas'})
    else:
        for i in fincas:
            listaFincas.append(list(i.values()))
        print(listaFincas)
        return jsonify({'response': 'cursos', 'fincas': listaFincas})

@app.route('/recomendar', methods=['POST'])
def recomendar():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    fincas = crudObj.traerFincasUsuario(documento, agricultorRaiz)
    fincasNombres = []
    for i in fincas:
        fincasNombres.append(i["nombre"])
    if fincas is None:
        return jsonify({'response': 'nofincas'})
    else:
        return jsonify({'response': 'cursos', 'fincas': fincasNombres})

@app.route('/recomendarcultivo', methods=['POST'])
def recomendarcultivo():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    fincaNombre = data_dic["finca"]
    basedatos = bd.BaseDatos()
    gestorOnto = go.GestorOntologia()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    _, reglaRaiz = basedatos.definir_raiz_reglas(conexion)
    _, cultivoRaiz = basedatos.definir_raiz_cultivos(conexion)
    cultivos = crudObj.traerCultivos(cultivoRaiz)
    reglas = crudObj.traerReglas(reglaRaiz)
    finca = crudObj.traerUnaFinca(documento, agricultorRaiz, fincaNombre)
    gestorOnto.adicionar_cultivos(cultivos)
    gestorOnto.adicionar_reglas(reglas)
    cultivos = gestorOnto.crear_conceptos(finca)
    if cultivos != []:
        return jsonify({'response': 'Success', 'cultivos': cultivos})
    else:
        return jsonify({'response': 'Error', 'mensaje': 'No se generaron recomendaciones'})

@app.route('/registrarFinca', methods=['POST'])
def registrarFinca():
    global conexion
    data = request.form
    data_dic = data.copy()
    documento = data_dic["documento"]
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    estado = crudObj.insertarFinca(documento, agricultorRaiz, data_dic)
    if estado:
        return jsonify({'response': 'Success'})
    else:
        return jsonify({'response': 'Error'})

@app.route('/registrarCultivo', methods=['POST'])
def registrarCultivo():
    global conexion
    data = request.form
    data_dic = data.copy()
    basedatos = bd.BaseDatos()
    crudObj = crud.Crud()
    gestorOnto = go.GestorOntologia()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, reglaRaiz = basedatos.definir_raiz_reglas(conexion)
    _, cultivoRaiz = basedatos.definir_raiz_cultivos(conexion)
    estado, cultivos = crudObj.insertarCultivo(cultivoRaiz, data_dic)
    id = crudObj.tomarID(cultivoRaiz)
    regla = gestorOnto.armar_regla(cultivos, id)
    estadoRegla = crudObj.insertarRegla(reglaRaiz, regla)
    if estado:
        if estadoRegla:
            return jsonify({'response': 'Success'})
        else:
            return jsonify({'response': 'Error'})
    else:
        return jsonify({'response': 'Error'})


"""
@app.route('/ert')
def inferirCultivo():
    global conexion
    datos = {"id":"1", "nombre": "Finca Chaques", "usuario": "123456"}
    crudObject = crud.Crud()
    basedatos = bd.BaseDatos()
    gestorOnto = go.GestorOntologia()
    basedatos.set_conexion(conexion)
    conexion = basedatos.get_conexion()
    _, agricultorRaiz = basedatos.definir_raiz_agricultores(conexion)
    _, reglaRaiz = basedatos.definir_raiz_reglas(conexion)
    _, cultivoRaiz = basedatos.definir_raiz_cultivos(conexion)
    cultivos = crudObject.traerCultivos(cultivoRaiz)
    reglas = crudObject.traerReglas(reglaRaiz)
    finca = crudObject.traerUnaFinca(datos["usuario"], agricultorRaiz, datos["nombre"])
    print(cultivos)
    print("----------")
    print(reglas)
    print("----------")
    print(finca)
    gestorOnto.adicionar_cultivos(cultivos)
    gestorOnto.adicionar_reglas(reglas)
    cultivos = gestorOnto.crear_conceptos(finca)
    print(cultivos)

#inferirCultivo()
"""

if __name__ == '__main__':
    app.run(debug=False)


"""basedatos = bd.BaseDatos()

conex = None

basedatos.set_conexion(conex)

conex = basedatos.get_conexion()

dataB, agric = basedatos.definir_raiz_agricultores(conex)

_,reglaRaiz = basedatos.definir_raiz_reglas(conex)
_, cultivoRaiz = basedatos.definir_raiz_cultivos(conex)


a = crud.Crud()

b = a.obtenerPasswordUsuario("123456", agric)

c = a.comprobarPassword(b, "martin147")

fincas = a.traerFincasUsuario("123456", agric)
print(fincas)


reglas = a.traerReglas(reglaRaiz)



cultivos = a.traerCultivos(cultivoRaiz)"""


