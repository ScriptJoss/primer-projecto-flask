# Importamos flask
from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

# Funcion generador contraseña
password_caract = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
def generar_password(length=12):
    password = ""
    for i in range(length):
        password += random.choice(password_caract)
    return password


@app.route("/")
def hello_world():
    return '''<h1>Web en flask por Joss</h1>
    <p>Esto es un parrafo</p>
    <a href="/random_fact">Random Fact</a>
    <a href="/password_generator">Genera contraseña aleatoria</a>
    '''

@app.route("/random_fact")
def random_fact():
    return f'''<h3>Algunos datos randoms</h3>
    <p>{random.choice(facts_list)}</p>
    <button><a href='/random_fact'>Ver otro dato</a></button>
    <a href="/">Regresar</a>
    '''

# Generador de contraseñas    
@app.route("/password_generator")
def password_generator():
    password = generar_password()
    return f'''<h3>Generador de contraseñas</h3>
                <p>La contraseña que generaste es: {password}</p>
                <a href="/">Regresar</a>
                '''


app.run(debug=True)
