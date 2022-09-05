#Clase generica para hacer un arbol
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

#Clase para arboles balanceados
class AVL_Tree(object):
  #Funcion para insertar un nodo, la funcion debe recibir el arbol y un int del nodo a insertar
	def insert(self, root, key):
		
		#Se inserta normal el nodo como si fuera un arbol binario de busqueda
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		#Se actualiza la altura del ancestro
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		#Se busca el factor de balanceo
		balance = self.getBalance(root)

		#Si esta desbalanceado:

    #Caso 1: Rotacion derecha
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		#Caso 2: Rotacion izquierda
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		#Caso 2: Rotacion doble derecha
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Caso 4: Rotacion doble izquierda
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

#Funcion para borrar un nodo, la funcion debe recibir el arbol y un int del nodo a borrar
	def delete(self, root, key):

		#Se borra como si fuera un arbol binario de busqueda normal
		if not root:
			return root

		elif key < root.val:
			root.left = self.delete(root.left, key)

		elif key > root.val:
			root.right = self.delete(root.right, key)

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp

			elif root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.getMinValueNode(root.right)
			root.val = temp.val
			root.right = self.delete(root.right,
									temp.val)


		if root is None:
			return root

    	#Se actualiza la altura del ancestro
		root.height = 1 + max(self.getHeight(root.left),
							self.getHeight(root.right))

		#Se saca el factor de balanceo
		balance = self.getBalance(root)

		#Se balancea dependiendo del factor de balanceo como en la parte de insercion
		
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)


		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)


		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)


		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root
#Funcion para rotar el arbol hacia la izquierda
	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		#Se rota el arbol
		y.left = z
		z.right = T2

		#Se actualizan las alturas
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

    #Se retorna el root
		return y
#Funcion para rotar el arbol hacia la derecha
	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		#Se rota el arbol
		y.right = z
		z.left = T3

		#Se actualizan las alturas
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		#Se retorna el root
		return y

  #Funcion para obtener la altura
	def getHeight(self, root):
		if not root:
			return 0

		return root.height

  #Funcion para obtener el factor de balanceo
	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root

		return self.getMinValueNode(root.left)

  #Funcion para ordenamiento de Preorden
	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.val), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)