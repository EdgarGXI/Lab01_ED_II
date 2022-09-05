from clases import *
from funciones import *


# -*- coding: utf-8 -*-
"""

#Punto 2: Árbol Espejo
"""

"""
Código usado para hacer el árbol espejo tiene como fuente
https://www.techiedelight.com/ para más información.

Además, y aquel que ayuda a imprimir el árbol fue tomado de
https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/

"""

#Creamos los nodos que vamos a utilizar
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

#Imprimimos
print("Árbol base:")    
print2DUtil(root,0)

print("Árbol Espejo:")    
convertToMirror(root)
print2DUtil(root,0)