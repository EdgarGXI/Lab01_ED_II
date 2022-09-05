COUNT = [10]


#Usamos la función para imprimir 
#el árbol para que sea visual para el usuario
def print2DUtil(root, space) :
 
    if (root == None) :
        return
 
    space += COUNT[0]
 
    print2DUtil(root.right, space)
 
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.key)
 
    print2DUtil(root.left, space)
 
def print2D(root) :
     
    print2DUtil(root, 2)

#Definimos la función espejo
def Mirror(root):
  #Comprobamos el caso en que la raíz
  #sea nula y retornamos la raíz de serlo
    if root is None:
        return
  #Usamos un temporal que tomara el valor 
  #de aquello que se encuentre a la izquierda
  #de la raíz del árbol
    tempmirror = root.left
  #Lo que esta a la izquierda se asignamos
  #el valor de aquello que se encuentre en 
  #la derecha
    root.left = root.right
  #Y lo qu esta en la derecha recibe el valor
  #de temp que contiene la información del
  #nodo de la izquierda
    root.right = tempmirror
 
 
# Función para convertir un árbol binario dado en su espejo
def convertToMirror(root):
 
    #Caso base: si el árbol está vacío
    if root is None:
        return
 
    #Le pasamos los valores que 
    #contiene el lado izquierdo
    convertToMirror(root.left)

    #Le pasamos los valores que
    #contiene el lado derecho
    convertToMirror(root.right)
 
    #Usamos la función mirror para 
    #invetir los valores
    Mirror(root)