import face_recognition as fr
import os

def reconhece_rosto(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos
    
    return False, []

def getRostos():
    rostos_reconhecidos = []
    nome_rostos = []

    rosto = []
    matricula = ""

    for arqs in os.walk(f'{os.curdir}'):
        for imgs in arqs[2]:
            rosto = reconhece_rosto(f"{imgs}")
            nome_rostos.append(f"{imgs}")
            rostos_reconhecidos.append(rosto[1][0])
    
    return rostos_reconhecidos, nome_rostos