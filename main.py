import PySimpleGUI as sg

layout = [
    [sg.Text('Check your License')], 
    [sg.Text('Login', size=(15,1)), sg.InputText()],
    [sg.Text('Password', size=(15,1)), sg.InputText()],
    [sg.Text('License Key', size=(15,1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]
#margins = (200,150)
window = sg.Window("License Check", layout, margins=(200,150))


event, values = window.read()

window.close()