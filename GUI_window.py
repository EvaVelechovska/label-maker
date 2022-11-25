import PySimpleGUI as sg

sg.theme("DarkBlue")

forma_choises = ["gtt", "sir", "sol"]
jednotka_choises = ["ml", "mg", "pcs"]


def welcoming_w():
    layout = ([sg.Text("Vítá Vás Label Maker", text_color="", font=("", 16), justification="Center")],
              [sg.Text("")],
              [sg.Push(), sg.Text("Jak chcete zadat štítky? ", font=(", 14")), sg.Push()],
              [sg.Push(), sg.Button("zadat ručně"), sg.Push()],
              [sg.Push(), sg.FileBrowse("Načíst ze soboru"), sg.Push()],
              [sg.Text("")],
              [sg.Button("Zavřít"), sg.Push(), sg.Button("Cancel")])

    window = sg.Window("Label maker", layout, size=(300, 250))
    while True:
        event, values = window.read()
        if event == "Cancel" or event == "Zavřít" or event == sg.WIN_CLOSED:
            break
        elif event == "zadat ručně":
            adding_w()

        elif event == "Načíst ze souboru":
            print("načteno a vyrobeno")

    window.close()
    return window


def adding_w():
    sg.theme("Darkblue")
    layout = [[sg.Menu(tool_bar_menu())],
              [sg.Frame("Zadejte", layout=[
                  [sg.Text("Název: ", size=(15, 1)), sg.InputText(key="název")],
                  [sg.Text("množství: ", size=(15, 1)), sg.InputText(key="množství")],
                  [sg.Text("jednotka: ", size=(15, 1)), sg.OptionMenu(jednotka_choises, key="jednotka")],
                  [sg.Text("forma: ", size=(15, 1)), sg.OptionMenu(forma_choises, key="forma")],
                  [sg.Text("cena: ", size=(15, 1)), sg.InputText(key="cena")]
              ]),
               sg.Frame("Zadané údaje", layout=[
                   [sg.Listbox(values=[], size=(50, 10), enable_events=True, select_mode="extended", key="list")]
               ])],

              [sg.Button("Ulož"), sg.Button("Další záznam"), sg.Button("Tisk"), sg.Push(), sg.Button("Zavři")]
              ]

    window = sg.Window("Zadejte", layout, finalize=True)
    while True:
        event, values = window.read()
        if event == "Zavři" or event == sg.WIN_CLOSED:
            break
        elif event == "Ulož":
            #  TODO: "rozdělit" sloupec aby zadané hodnoty byly v řádce a ne sloupci
            zadane = []
            zadane.append(values)
            # zadane.append(values["množství"])
            # zadane.append(values["jednotka"])
            # zadane.append(values["forma"])
            # zadane.append(values["cena"])
            window["list"].update(zadane)
            print("zadáno", values)
        elif event == "Další záznam":
            #  TODO: zařídít, aby se další záznamy přídávaly pod sebe
            zadane = []
            zadane.append(values["název"]), zadane.append(values["množství"]),
            zadane.append(values["jednotka"])
            zadane.append(values["forma"])
            zadane.append(values["cena"])
            window["list"].update(zadane)
            # uložý co je napsáno a vyprázdní okýnka
            window["název"].Update("")
            window["množství"].Update("")
            window["jednotka"].Update("")
            window["forma"].Update("")
            window["cena"].Update("")
            print(values, "další záznam")

    window.close()

    return window


def tool_bar_menu():
    menuBar_Layout = [
        ['&File', ['&Otevřít     Ctrl-O', '&Uložit       Ctrl-S', '&Vlastnosti', 'E&xit']],
        ['&Edit', ['Zpět']],
        ['&Toolbar', ['---', 'Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
        ['&Help', ['&About...']]
    ]
    return menuBar_Layout
