import PySimpleGUI as sg

sg.theme('DarkPurple4')   # Add a touch of color

title_font = ('Courier',20)
# All the stuff inside your window.
layout = [  [sg.Text('Menos é Mais', justification='center', size=(100,1), font=title_font)],
            [sg.Button('Cadastrar rosto'), sg.Button('Cancel')], ]

# Create the Window
window = sg.Window('Menos é Mais', layout, size=(800,600), resizable=True, grab_anywhere=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()