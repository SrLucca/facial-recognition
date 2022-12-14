import cv2
import os
from picture import register_face
import time

ROOT_DIR = os.path.abspath(os.curdir)

def new_user(matricula):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()

    if result:

        os.chdir(fr'{ROOT_DIR}\img')
        cv2.imshow(f"{matricula}", image)

        cv2.imwrite(f"{matricula}.png", image)

        time.sleep(2)
        
        register_face(matricula)

        cv2.waitKey(0)
        cv2.destroyWindow("Foto novo usuario")

    else:
        print("Imagem não detectada, tente novamente!")

    os.chdir(ROOT_DIR)
    return