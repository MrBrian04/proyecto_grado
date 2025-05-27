from flask import Flask, render_template, request, redirect, url_for
from backend import db, Compra, Usuario
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'  # Cambia si usas MySQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('menu.html')

    @app.route('/comprar', methods=['GET', 'POST'])
    def comprar():
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            celular = request.form['celular']
            cantidad = request.form['cantidad']

            nueva_compra = Compra(
                nombre=nombre,
                apellido=apellido,
                celular=celular,
                cantidad=cantidad
            )
            db.session.add(nueva_compra)
            db.session.commit()
            return redirect(url_for('historial'))
        return render_template('Registro.html')

    @app.route('/historial')
    def historial():
        compras = Compra.query.all()
        return render_template('historial.html', compras=compras)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)