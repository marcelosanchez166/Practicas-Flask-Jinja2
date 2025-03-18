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



if __name__ == "__main__":
  app.run(debug=True, port=5001)