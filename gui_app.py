import logging

import PySimpleGUI as sg

log = logging.getLogger(__name__)

log = logging.getLogger(__name__)


class GUIApp:

    def __init__(self):
        self.in_files = []
        self.user_labels = []
        self.event_to_action = {
        }
        self.table_header_to_key = {
        }

    def __enter__(self):
        self.window = self.create_window()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.window.close()

    def __eat_events__(self):
        """Eats falsely fired events
        NOTE: https://github.com/PySimpleGUI/PySimpleGUI/issues/4268
        """
        while True:
            event, values = self.window.read(timeout=0)
            if event == '__TIMEOUT__':
                break
        return

    def run(self):
        while True:
            event, values = self.window.read()
            log.debug((event, values))

            if event == sg.WIN_CLOSED:  # always,  always give a way out!
                break

            # do actions
            try:
                self.event_to_action[event](values)
                self.__eat_events__()
            except KeyError:
                log.exception('unknown event')

    def create_window(self):
        layout = ([sg.Text("Vítá Vás Label Maker", text_color="", font=("", 16), justification="Center")],
                  [sg.Text("")],
                  [sg.Push(), sg.Text("Jak chcete zadat štítky? ", font=", 14"), sg.Push()],
                  [sg.Push(), sg.Button("zadat ručně"), sg.Push()],
                  [sg.Push(), sg.FileBrowse("Načíst ze soboru"), sg.Push()],
                  [sg.Text("")],
                  [sg.Push(), sg.Button("Exit")])

        return sg.Window("Label maker", layout, size=(300, 250))


def gui_main():
    log.info('starting gui app')

    with GUIApp() as gui:
        gui.run()

    return 0
