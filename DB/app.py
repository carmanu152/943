from flask import Flask,request
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba_python'

mysql = MySQL(app)



@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from usuarios;")
    #Datos = lista2D, tiene filas y columnas y se maneja con dos coordenadas
    #datos[posFila][posColumna]
    #nombre = datos[0][1]
    datos = cursor.fetchall()
    resultado = json.dumps(datos)#resultado = '[[1,"carlos","nuñez",27],[2,"andres","velez",20]]'
    
    return resultado

@app.route("/user")
def user():
    id = 1
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from usuarios where ID = {id}")
    fila = cursor.fetchone() #  fila = [1,"carlos","nuñez",27]
    #nombre = fila[1]
    resultado = json.dumps(fila)
    return resultado

@app.route("/insertar", methods=["POST"])
def insertar():

    json_datos = request.get_json()


    nombre = json_datos["nombre"]
    apel = json_datos["apellido"]
    edad = json_datos["edad"]
    
    cursor =  mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios ( Nombre, Apellido, Edad) VALUES ( %s, %s, %s)",(nombre,apel,edad))

    cursor.connection.commit()
    return "Aceptado"

if __name__ == "__main__":
    app.run(debug=True,port=5000)