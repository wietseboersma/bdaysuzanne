from flask import Flask
import time
import random
import os

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
            output += '<span style="color: {};">{}</span>'.format(random_color.split('[')[-1].split('m')[0], char)
            time.sleep(0.1)  
        output += "<br>"
    
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
