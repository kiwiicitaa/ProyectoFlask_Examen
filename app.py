from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad= int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            "nombre": nombre,
            "total": total_sin_descuento,
            "total_final": total_con_descuento,
        }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        mensaje = ""

        if usuario == 'juan' and password == 'admin':
            mensaje = "Bienvenido administrador Juan"
        elif usuario == 'pepe' and password== 'user':
            mensaje = "Bienvenido usuario Pepe"
        else:
            mensaje = "Nombre de usuario o contraseña incorrecto"
        return render_template('resultado2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
        app.run(debug=True)

