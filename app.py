from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)


"""Practicando COOKIES"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        
        # procesar los datos aquí
        print(f'Hola {name}')
        response = make_response(render_template('index.html', name=name))#crea la cookie en el servidor y la envia al cliente para que se guarde en el navegador del usuario 
        expires = datetime.datetime.now() + datetime.timedelta(days=365)
        response.set_cookie('name', name, expires=expires)# establece la cookie con el nombre "name" y el valor "name" y la fecha de expiración en 365 días 
        return response
    else:
      # Get the name from cookie if it exists
      name = request.cookies.get('name')#devuelve el valor de la cookie si existe, de lo contrario, devuelve None. cuando el usuario abre la página por primera vez, no hay cookie, por lo que devuelve None y se muestra el formulario vacío. cuando el usuario envía el formulario, se crea la cookie con el nombre "name" y el valor "name" y la fecha de expiración en 365 días. cuando el usuario vuelve a abrir la página, la cookie existe y se muestra el formulario con el nombre prellenado.
      return render_template('index.html', name=name)



"""Obteniendo Datos de Formularios de distinto metodo y formas de enviarlos

---Metodos:
  - GET: 
      envía los datos en la URL (visible en la URL) (se utiliza para enviar datos no sensibles)

  - POST, PUT, DELETE: 
      envía los datos en el cuerpo de la petición HTTP (no visible en la URL) (se utiliza para enviar datos sensibles)

metodos Python Para obtener los datos de un formulario
-- GET : 
request.args.get('nombre')

-- POST, PUT, DELETE, PATCH :
  Obtener datos individuales get:
    # request.form.get('nombre'), request.json.get('nombre'), request.data.get('nombre'), request.values.get('nombre') ===> mas seguro, ya que se puede verificar si el campo existe o no, si no existe, devuelve None
    # request.form['nombre'], ===> menos seguro , ya que no se puede verificar si el campo existe o no, si no existe, devuelve una excepcion KeyError 
    # request.json['nombre'], request.data['nombre'], request.values['nombre'] 
    # request.form.getlist('nombre'), request.json.getlist('nombre'), request.data.getlist('nombre'), request.values.getlist('nombre')"""


#Pasando datos a las plantillas
personas = {"Nombre": "Marcelo", "Apellido": "Sanchez", "Edad": 29, "Dirección":"Santa Ana"}
marcasVehiculos = ["Volvo", "Mercedes", "Jaguar", "Nissan", "Toyota", "Audi", "Kia", "Mazda", "Honda", ]


@app.route("/datos", methods=["GET", "POST"])
def datos():
  if request.method =="POST":
    genero = request.form.get('genero')
    vehiculo1 = request.form.get("vehicle1")
    vehiculo2 = request.form.get("vehicle2")
    vehiculo3 = request.form.get("vehicle3")
    automovil = request.form.get("cars")
    personas["Genero"] = genero#Agregando el genero enviado desde el formulario hacia el diccionario personas
    opciones = request.form.getlist("opciones")#Obteniendo los datos de las opciones seleccionadas en el formulario
    #selectmultiples = request.form.getlist("opcionesmultipleselect")#obteniendo el select multiple como una lista
    selectmultiples = request.form.get("opcionesmultipleselect")#obteniendo el select multiple como valor de un solo elemento
    print(type(selectmultiples), "tipo de objeto que se obtiene al seleccionar selectmultiples en el formulario")
    for i in range(len(selectmultiples)):
      print(selectmultiples[i], "opcion seleccionada en el formulario")
    if vehiculo1:
      personas['Vehiculo'] = vehiculo1
    elif vehiculo2:
      personas["Vehiculo"] = vehiculo2
    elif vehiculo3:
      personas["Vehiculo"] = vehiculo3
    return render_template("datos.html", personas=personas, marcasVehiculos=marcasVehiculos, automovil=automovil, opciones=opciones, selectmultiples=selectmultiples)
  else:
    return render_template("datos.html", personas=personas, marcasVehiculos=marcasVehiculos)



@app.route('/dias', methods=["GET",'POST'])
def dias():
    datos_dias = []
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    # Procesar cada día de la semana
    if request.method == 'POST':
      for dia in days :
        #los valores se obtienen del formulario y la variable dia es el valor la lista de dias llamada days
          if request.form.get(f'dia_{dia}'):  # Verifica si el día fue seleccionado
              hora_inicio = request.form.get(f'hora_inicio_{dia}')
              hora_fin = request.form.get(f'hora_fin_{dia}')
              prioridad = request.form.get(f'prioridad_{dia}')
              notas = request.form.get(f'notas_{dia}')
              comentarios = request.form.get(f'comentarios_{dia}')

              # Almacena los datos del día en un diccionario
              dia_data = {
                  'dia': dia.capitalize(),
                  'hora_inicio': hora_inicio,
                  'hora_fin': hora_fin,
                  'prioridad': prioridad,
                  'notas': notas,
                  'comentarios': comentarios
              }
              datos_dias.append(dia_data)
      # Renderiza los datos o haz otra cosa con ellos
      print(datos_dias)
      return render_template("dias.html",datos_dias=datos_dias)
    else:
      return render_template("dias.html",datos_dias=datos_dias, days=days)


ventas = {
  "vendedor1": {"nombre":"Juan", "id": 1, "producto": "Camiseta", "cantidad": 2, "precio": 10.99},
  "vendedor2": {"nombre":"Marco", "id": 2, "producto": "Pantalón", "cantidad": 1, "precio": 29.99}, 
  "vendedor3": {"nombre":"Lucas", "id": 3, "producto": "Zapatos", "cantidad": 3, "precio": 39.99},
  }

print(type(ventas))
@app.route('/prueba', methods=['POST', 'GET'])
def prueba():
  diccionario_horarios = {}
  if request.method == 'POST':
    days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    for dia in days:
      if request.form.get(f'dias[{dia}]'):
        hora_inicio = request.form.get(f'horas[{dia}][inicio]')
        hora_fin = request.form.get(f'horas[{dia}][fin]')
        diccionario_horarios[dia] = {
          "hora_inicio": hora_inicio,
          "hora_fin": hora_fin
          }
    print(diccionario_horarios)
    return render_template('agrupandoelementos.html', diccionario_horarios=diccionario_horarios, ventas=ventas)
  return render_template('agrupandoelementos.html', diccionario_horarios=diccionario_horarios, ventas=ventas)


if __name__ == "__main__":
  app.run(debug=True, port=5001)