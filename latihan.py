import PySimpleGUI as sg
sg.theme("DarkBlue9")  
sg.theme_text_color ("#FFFF00")
window = sg.Window(title ="Profile", 
                    layout =   [[sg.Text("NPM        : 2210010492")],
                                [sg.Text("NAMA    : Geraldi Fikri haiqal  ")],
                                [sg.Text("Kelas        : 5E Reguler Banjarmasin")],
                                [sg.Text("Matkul     : Pemrograman visual 3")]
                                ],
                    size=(400,200),
                    font=("Times", 18))
window()
Window.close()