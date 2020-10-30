from flask import Flask, render_template
from datetime import date
from random import choice

app = Flask(__name__)

reglas = {
    'piedra': {
        'piedra': {'resultado': 0, 'mensaje': 'Ninguno gana'},
        'papel': {'resultado': -1, 'mensaje': 'Papel envuelve piedra'},
        'tijeras': {'resultado': 1, 'mensaje': 'Piedra aplasta tijeras'},
        'lagarto': {'resultado': 1, 'mensaje': 'Piedra aplasta lagarto'},
        'spock': {'resultado': -1, 'mensaje': 'Spock vaporiza piedra'}
    },
    'papel': {
        'piedra': {'resultado': 1, 'mensaje': 'Papel envuelve piedra'},
        'papel': {'resultado': 0, 'mensaje': 'Nadie gana'},
        'tijeras': {'resultado': -1, 'mensaje': 'Tijeras cortan papel'},
        'lagarto': {'resultado': -1, 'mensaje': 'Lagarto devora papel'},
        'spock': {'resultado': 1, 'mensaje': 'Papel desautoriza spock'}
    },
    'tijeras': {
        'piedra': {'resultado': -1, 'mensaje': 'Piedra aplasta tijeras'},
        'papel': {'resultado': 1, 'mensaje': 'Tijeras corta papel'},
        'tijeras': {'resultado': 0, 'mensaje': 'Nadie gana'},
        'lagarto': {'resultado': 1, 'mensaje': 'Tijeras decapitan lagarto'},
        'spock': {'resultado': -1, 'mensaje': 'Spock rompe tijeras'}
    },
    'lagarto': {
        'piedra': {'resultado': -1, 'mensaje': 'Piedra aplasta lagarto'},
        'papel': {'resultado': 1, 'mensaje': 'Lagarto devora papel'},
        'tijeras': {'resultado': -1, 'mensaje': 'Tijeras decapitan lagarto'},
        'lagarto': {'resultado': 0, 'mensaje': 'Nadie gana'},
        'spock': {'resultado': 1, 'mensaje': 'Lagarto envenena spock'}
    },
    'spock': {
        'piedra': {'resultado': 1, 'mensaje': 'Spock vaporiza piedra'},
        'papel': {'resultado': -1, 'mensaje': 'Papel desautoriza spock'},
        'tijeras': {'resultado': 1, 'mensaje': 'Spock rompe tijeras'},
        'lagarto': {'resultado': -1, 'mensaje': 'Lagarto envenena spock'},
        'spock': {'resultado': 0, 'mensaje': 'Nadie gana'}
    }
}

objetos = list(reglas.keys())

@app.route('/')
def inicio():
    fecha = date.today()

    return render_template(
        'selecciona_tiro.html',
        fecha=fecha)

@app.route('/tiro/<tiro_jugador>')
def tiro(tiro_jugador):
    tiro_compu = choice(objetos)
    resultado = reglas[tiro_jugador][tiro_compu]['resultado']
    mensaje = reglas[tiro_jugador][tiro_compu]['mensaje']

    return render_template(
        'despliega_resultado.html',
        tiro_jugador = tiro_jugador,
        tiro_compu = tiro_compu,
        resultado = resultado,
        mensaje = mensaje)