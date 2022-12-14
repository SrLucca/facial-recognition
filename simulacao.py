import PySimpleGUI as sg
from send_email import send_warning
from webcam import recognition
from db_connector import wrning_connection

sg.theme('DarkPurple4')   # Add a touch of color

title_font = ('Courier',20)
# All the stuff inside your window.
layout = [  [sg.Text('Menos é Mais', justification='center', size=(100,1), font=title_font)],
            [sg.Text("")],
            [sg.Text("Peso jogado fora"), sg.Input()],
            [sg.Button('Simular', size=(100,1))],
            [sg.Button('Cancel', size=(100,1))], ]

# Create the Window
window = sg.Window('Menos é Mais', layout, size=(400,200), resizable=True, grab_anywhere=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    else:
        matricula = recognition()
        matricula_corrigida = matricula.split(".")
        peso = int(values[0])
        if peso >= 300:
            dados_usuario = wrning_connection(int(matricula_corrigida[0]))
            send_warning(dados_usuario[0], peso, dados_usuario[1])
        else:
            pass

window.close()