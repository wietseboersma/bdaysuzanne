import time
import random

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

for zin in zinnen:
    for char in zin:  
        random_color = random.choice(kleuren)
        print(random_color + char + reset_kleur, end='', flush=True)
        time.sleep(0.1)  
    print("\n")  
