import PySimpleGUI as sg
from take_photo import new_user

sg.theme('DarkPurple4')   # Add a touch of color

title_font = ('Courier',20)
# All the stuff inside your window.
layout = [  [sg.Text('Menos é Mais', justification='center', size=(100,1), font=title_font)],
            [sg.Text("")],
            [sg.Text("Matricula"), sg.Input()],
            [sg.Button('Cadastrar rosto', size=(100,1))],
            [sg.Button('Cancel', size=(100,1))], ]

# Create the Window
window = sg.Window('Menos é Mais', layout, size=(400,200), resizable=True, grab_anywhere=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    else:
        new_user(values[0])
        print('You entered ')

window.close()