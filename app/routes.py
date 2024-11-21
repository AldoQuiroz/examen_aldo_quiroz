from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        quantity = int(request.form['quantity'])
        price_per_can = 9000

        total_without_discount = quantity * price_per_can

        # Calcular descuento
        if age >= 18 and age <= 30:
            discount = 0.15
        elif age > 30:
            discount = 0.25
        else:
            discount = 0.0

        discount_amount = total_without_discount * discount
        total_with_discount = total_without_discount - discount_amount

        return render_template('result.html', name=name, total_without_discount=total_without_discount,
                               discount_amount=discount_amount, total_with_discount=total_with_discount)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Lógica de autenticación
        if username == 'juan' and password == 'admin':
            message = f"Bienvenido administrador {username}"
        elif username == 'pepe' and password == 'user':
            message = f"Bienvenido usuario {username}"
        else:
            message = "Usuario o contraseña incorrectos"

        return render_template('result2.html', message=message)
    return render_template('ejercicio2.html')




