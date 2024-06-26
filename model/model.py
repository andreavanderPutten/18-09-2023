import networkx as nx

from database.DAO import DAO
from database.DB_connect import DBConnect


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()


    def creaGrafo(self, nazione, anno):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getNodi(nazione))
        self.grafo.add_nodes_from(DAO.getArchi(nazione,anno))



    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def top5Nodi(self):
        lista = []
        for nodo in self.grafo.nodes:
            if self.grafo.out_degree(nodo) == 0:
                lista.append((self.grafo.in_degree(nodo), nodo))
        lista.sort(reverse=True)
        return lista
