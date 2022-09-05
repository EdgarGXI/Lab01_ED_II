
#Funcion para imprimir el arbol por orden de nivel  
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Funcion para imprimir los nodos en un nivel
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
 

 
#Funcion para la altura
def height(node):
    if node is None:
        return 0
    else:
        #Sacamos la altura de los hijos, de forma recursiva
        lheight = height(node.left)
        rheight = height(node.right)
 
        #El resultado mas grande es el que usaremos
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

#Funcion para saber si un nodo esta en el arbol, toma como parametro el arbol y el nodo a buscar
def ifNodeExists(node, key):
 
    if (node == None):
        return False
 
    if (node.val == key):
        return True
 
    # De forma recursiva revisamos el hijo izquierdo
    res1 = ifNodeExists(node.left, key)

    if res1:
        return True
 
    # Si no se encuentra en la izquierda, entonces, de forma recursiva revisamos el hijo derecho
    res2 = ifNodeExists(node.right, key)
 
    return res2

#Funcion para buscar la altura del nodo
def findHeightUtil(root, x):
    global height1
  

    if (root == None):
        return -1
  
    #Buscamos la altura para los hijos izquierdo y derecho
    leftHeight = findHeightUtil(root.left, x)
  
    rightHeight = findHeightUtil(root.right, x)
  
    #Se computa el resultado
    ans = max(leftHeight, rightHeight) + 1
  

    if (root.val == x):
        height1 = ans
  
    return ans
  
#Funcion/Wrapper pa encontar la altura de un nodo
def findHeight(root, x):
    global height1

    maxHeight = findHeightUtil(root, x)
  
    return height1

#Funcion para el abuelo de un nodo, requiere del nodo a buscar y del arbol
def abuelo(root, val):

    if root is None:
        return
    #Se crea un vector en el que se van almacenando los nodos
    nodeStack = []
    nodeStack.append(root)
 
    while(len(nodeStack) > 0):
        #Sacamos el ultimo elemento del vector y lo almacenamos en una variable 
        node = nodeStack.pop()
         
        #Agregamos al vector
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
      #Comparamos que el nodo actual tenga hijos
        if (node.left != None and
            node.right != None):
           #Verificamos que el nodo actual tenga nietos
            if (node.left.left != None or
                node.left.right != None or
                node.right.left != None or
                node.right.right != None):
              #Buscamos si nuestro nodo de busqueda es el nieto de nuestro nodo actual
                if(node.left.left != None):
                    if(node.left.left.val == val):
                        return node.val
                if(node.left.right != None):
                    if (node.left.right.val == val):
                        return node.val
                if(node.right.left != None):
                    if (node.right.left.val == val):
                        return node.val
                if(node.right.right != None):
                    if(node.right.right.val == val):
                        return node.val

#Funcion para el tio de un nodo, requiere del nodo a buscar y del arbol
def tio(root, valtio):

    if root is None:
        return
    #Se crea un vector en el que se van almacenando los nodos
    Stack = []
    Stack.append(root)
 
    while(len(Stack) > 0):
        #Sacamos el ultimo elemento del vector y lo almacenamos en una variable 
        kl = Stack.pop()
         
        #Agregamos al vector
        if kl.right is not None:
            Stack.append(kl.right)
        if kl.left is not None:
            Stack.append(kl.left)
        #Comparamos que el nodo actual tenga hijos
        if (kl.left != None and
            kl.right != None):
           #Verificamos que el nodo actual tenga nietos
            if (kl.left.left != None or
                kl.left.right != None or
                kl.right.left != None or
                kl.right.right != None):
              #Si el nodo que estamos buscando es el nieto del nodo temporal,
              #entonces el tio sera el hijo contrario del nodo temporal comparado
              #al nodo de busqueda, es decir, si el nodo de busqueda es el nieto
              #en el subarbol izquierdo del nodo temporal, entonces el tio sera,
              #el hijo derecho del nodo temporal, y viceversa
              if(kl.left.left != None and kl.left.left.val == valtio):
                  if(kl.right != None):
                    return kl.right.val
              if(kl.left.right != None and kl.left.right.val == valtio):
                  if(kl.right != None):
                    return kl.right.val
              if(kl.right.left != None and kl.right.left.val == valtio):
                  if(kl.left != None):
                    return kl.left.val
              if(kl.right.right != None and kl.right.right.val == valtio):
                  if(kl.left != None):
                    return kl.left.val


#Funcion que imprime el arbol en la terminal
COUNT = [10]
def print2DUtil(root, space) :
 
    if (root == None) :
        return
 
    space += COUNT[0]
 
    print2DUtil(root.right, space)
 

    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper para la funcion print2DUtil()
def print2D(root) :
     
    
    print2DUtil(root, 2)