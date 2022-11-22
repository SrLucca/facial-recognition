import face_recognition as fr
from engine import reconhece_rosto, getRostos

def register_face(matricula):

    desconhecido = reconhece_rosto(f"{matricula}.png")

    if desconhecido[0]:
        rosto_desconhecido = desconhecido[1][0]
        rostos_conhecidos, nome_rostos = getRostos()
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print("resultados = ",resultados)

        for i in range(len(nome_rostos)):
            resultado = resultados[i]
            if(resultado):
                print(f"Rosto do {matricula} foi reconhecido")
    return