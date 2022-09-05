from clases_princ import *
from metodos_extra import *


# -*- coding: utf-8 -*-
"""


Referencias:
https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/



#Punto 1: Árbol Autobalanceo
"""



#Creamos el arbol
myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
	root = myTree.insert(root, num)


print("\n")
print("\n")


print()
#Se imprime el arbol
print2D(root)

## Codigo driver

bandera=1
while(bandera!=0):
  print("Que desea hacer?, 1: Insertar un nodo, 2: Eliminar un nodo, 3: Buscar un nodo, 4: Mostrar el recorrido por nivel, \n 5: Mostrar la altura de un nodo, 6: Encontar el abuelo de un nodo, 7: Encontar el tio de un nodo, 0: Salir ")
  bandera=int(input())
  print("\n")
  print("\n")
  if(bandera==1):
    num=int(input("Inserte el valor del nodo a ingresar "))
    while(ifNodeExists(root, num)):
      num=int(input("El valor ya se encuentra en el arbol, por favor ingrese uno diferente "))
    root = myTree.insert(root, num)
    print2D(root)
    print("\n")
    print("\n")
  if(bandera==2):
    num=int(input("Inserte el valor del nodo a eliminar "))
    while(not ifNodeExists(root, num)):
      num=int(input("El valor no se encuentra en el arbol, por favor ingrese uno diferente "))
    root = myTree.delete(root, num)
    print2D(root)
    print("\n")
    print("\n")
  if(bandera==3):
      num=int(input("Inserte el valor del nodo a buscar "))
      
      if (ifNodeExists(root, num)):
        print("El nodo, ", num, " SI existe")
      else:
        print("El nodo, ", num, " NO existe")
      print("\n")
      print("\n")
  if(bandera==4):
    print2D(root)
    print("El recorrido por nivel del arbol es")
    printLevelOrder(root)
    print("\n")
    print("\n")
  if(bandera==5):
    x=int(input("Inserte el nodo que desea saber su altura "))
    while (not ifNodeExists(root, x)):
      x=int(input("Inserte el nodo que desea saber su altura "))

    print("La altura de ", x, "es ",findHeight(root,x))
    print("\n")
    print("\n")
  if(bandera==6):
    x=int(input("Inserte el nodo que desea saber su abuelo "))
    print("El abuelo de ", x , " es ",abuelo(root,x))
    print("\n")
    print("\n")
  if(bandera==7):
    x=int(input("Inserte el nodo que desea saber su tio "))
    print("El tio de ", x , " es ",tio(root,x))
    print("\n")
    print("\n")
  if(bandera==0):
    print("Hasta luego")
    bandera=-1
    break
  if(bandera > 7 or bandera < 0 ):
    bandera=input("Por favor ingrese un numero valido")
