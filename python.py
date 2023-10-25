from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def birthday_greeting():
    zinnen = [
        'Hieperdepiep?',
        'Hoera!',
        'Hieperdepiep?',
        'Hoera!',
        'Hieperdepiep?',
        'Hoeraaaaaaa!',
        'Een fijne verjaardag gewenst -turend over de velden met een whisky in je hand!'
    ]

    kleuren = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  
    reset_kleur = '\033[0m'  

    output = ""
    for zin in zinnen:
        for char in zin:  
            random_color = random.choice(kleuren)
            output += random_color + char + reset_kleur
            time.sleep(0.1)  
        output += "\n"
    
    return '<pre>' + output + '</pre>'

if __name__ == '__main__':
    app.run(debug=True)

