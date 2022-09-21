import face_recognition as fr

def reconhece_rosto(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos
    
    return False, []

def getRostos():
    rostos_reconhecidos = []
    nome_rostos = []

    eu = reconhece_rosto("./img/eu.jpeg")

    if eu[0]:
        rostos_reconhecidos.append(eu[1][0])
        nome_rostos.append("Lucca")
    
    return rostos_reconhecidos, nome_rostos