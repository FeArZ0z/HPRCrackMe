import PySimpleGUI as sg
import traceback

layout = [
    [sg.Text('Check your License')], 
    [sg.Text('Login', size=(15,1)), sg.InputText()],
    [sg.Text('Password', size=(15,1)), sg.InputText()],
    [sg.Text('License Key', size=(15,1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]
#margins = (200,150)
window = sg.Window('License Check', layout, margins=(200,150))

try:
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            if values[0].size == 0:
                window['-OUT-'].update(values['-IN-'])
    window.close()
except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened!', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURED!', e, tb)

