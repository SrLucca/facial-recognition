import face_recognition as fr
from engine import reconhece_rosto, getRostos

desconhecido = reconhece_rosto("./img/desconhecido.JPG")

if desconhecido[0]:
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nome_rostos = getRostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(nome_rostos)):
        resultado = resultados[i]
        if(resultado):
            print(f"Rosto do {nome_rostos} foi reconhecido")