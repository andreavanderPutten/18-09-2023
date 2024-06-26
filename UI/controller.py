import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        anni = DAO.getAnni()
        nazioni = DAO.getNazioni()

        self._view._ddyear.options = list(map(lambda x: ft.dropdown.Option(x),anni))
        self._view._ddnazioni.options = list(map(lambda x: ft.dropdown.Option(x), nazioni))

    def handle_graph(self, e):
        anno = int(self._view._ddyear.value)
        nazione = str(self._view._ddnazioni.value)

        self._model.creaGrafo(nazione,anno)
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi : {self._model.grafoDetails[0]} Numero di archi : {self._model.grafoDetails[1]}"))
        self._view.page.update()

    def handle_search(self, e):
        pass