# Importamos flask
from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route("/")
def hello_world():
    return '''<h1>Web en flask por Joss</h1>
    <p>Esto es un parrafo</p>
    <a href="/random_fact">Random Fact</a>
    '''

@app.route("/random_fact")
def random_fact():
    return f'''<h3>Algunos datos randoms</h3>
    <p>{random.choice(facts_list)}</p>
    <button><a href='/random_fact'>Ver otro dato</a></button>
    <a href="/">Regresar</a>
    '''

app.run(debug=True)