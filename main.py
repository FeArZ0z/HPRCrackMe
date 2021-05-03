import PySimpleGUI as sg

layout = [[sg.Text("Check your License")], [sg.Button("OK")]]
#margins = (200,150)
window = sg.Window("License Check", layout, margins=(200,150))

while True:
    event, values = window.read()
    if event =="OK" or event == sg.WIN_CLOSED:
        break


window.close()