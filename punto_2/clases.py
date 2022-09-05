#Creamos la clase Nodo con su constructor
#y sus atributos serán k, right, y left


class Node:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None
