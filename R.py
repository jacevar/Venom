import pyrebase
import RPi.GPIO as GPIO
import time

microphone = 18 
GPIO.setmode(GPIO.BOARD)
# GPIO.setup(Led,GPIO.OUT)

cred ={
  "apiKey":"AIzaSyCPjBU8uKCuQn-U_yhODASgyLgtcWAfKyU",
  "authDomain": "venom-293e9.firebaseapp.com",
  "projectId": "venom-293e9",
  "storageBucket":"venom-293e9.appspot.com",
  "databaseURL":"https://venom-293e9-default-rtdb.firebaseio.com"
  }
firebase = pyrebase.initialize_app(cred)

db = firebase.database()
commands = db.child("commands")
"""
commands.update({
                    "reproducir cancion": {
                        "accion": "conectar con spotify",
                        "objeto": "spotify API"
                    }
                })
"""

def stream_handler(message):
    message = message["data"]
    print(message)

mystream = commands.stream(stream_handler)
"""
docs = commands.get().val()
for doc in docs:
    print(doc, docs[doc])
"""
mystream.close()