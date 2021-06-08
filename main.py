import PySimpleGUI as sg
import traceback
import base64
# input fields and Layout for the Window
layout = [
    [sg.Text('Check your License')], 
    [sg.Text('Username', size=(15,1)), sg.InputText()],
    [sg.Text('Password', size=(15,1)), sg.InputText()],
    [sg.Text('License Key', size=(15,1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]

window = sg.Window('License Check', layout, margins=(200,150))

try:
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            if len(values[0]) == 0 or len(values[1]) == 0 or len(values[2]) == 0:
                sg.Popup('Please fill all fields')
            else:
                #TODO: implement License Key validation
                # String builder from input encode in b64 and compare
                # if not the same: Contacting Server, if the same Success message
                joinedWords = values[0] + ',' + values[1] + ',' + values[2]
                encodedWords = base64.b64encode(joinedWords.encode("utf-8"))
                #sg.Popup(encodedWords)
                #licenseBase = "johndoe,rottenTomatoes24,1234-DEAD-BEEF-5678"
                #validLicense = base64.b64encode(licenseBase.encode("utf-8"))
                validLicense = b'am9obmRvZSxyb3R0ZW5Ub21hdG9lczI0LDEyMzQtREVBRC1CRUVGLTU2Nzg='
                # Check if input == license


                if (encodedWords == validLicense):#
                    sg.Popup('You Hacked the World')
                else:
                    sg.Popup('Contacting Server, this may take a while.')
                    #sg.Popup(encodedWords + '   ' + validLicense)
        if event == 'Cancel':
            break
    window.close()

#Error Handling    
except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened!', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURED!', e, tb)

