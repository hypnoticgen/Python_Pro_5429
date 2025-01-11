meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Nashe": "algo asombroso o bueno esta pasando",
            "OMG": "expresion de asombro",
            "WTF": "Que carajos",
            "Aesthetic": "expresion para definir cierto estilo",
            "GRWM": "expresion usada para indicar alistate conmigo",
            "NEA": "persona con el corte de cabello del 7",
            "BRUH": "expresion utilizada para multiples cosas",
            "GG": "Great Game",
            "Shippear": "armar parejas falsas",
            "PRIME": "estar en su mejor momento",
            "HYPE": "emocion grande llegando a la euforia",
            "F": "pasa una situacion lamentable"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
  print (aqui esta el significado de tu palabra: , meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("ya que no lo tengo, preguntale a google")
