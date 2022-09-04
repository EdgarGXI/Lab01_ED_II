# https://www.geeksforgeeks.org/insertion-in-a-b-tree/
MAX = 2

class Node:
    """
    A class for a node of a B+ tree.
    
    Attributes:
        IS_LEAF (boolean): Indicates if node is a leaf node.
        keys (list): Contains keys.
        size (int): Current size of the node (amount of keys).
        pointers (list): Contains children.
    """
    
    def __init__(self):
        self.IS_LEAF = False
        self.keys = [None]*MAX
        self.size = 0
        self.pointers = [None]*(MAX+1)
        
        
class BPlusTree:
    """
    A class for a B+ tree.
    
    Attributes:
        root (Node): The root of the tree.
    
    Methods:
        print_tree(): Prints tree nodes.
        insert(x): Inserts input data into the tree as a leaf node.
        insertInternal(x, cursor, child): Inserts input data into cursor keys and adds child to its children.
        findParent(cursor, child): Finds and returns parent node of input child.
    """
    
    def __init__(self) -> None:
        self.root = None
                   
    def print_tree(self):
        """
        Prints tree nodes following the format:
        Leaf/Internal Node: (pointers[0]) keys[0] (pointers[1]) keys[1] ... keys[node.size] (pointers[node.size+1])
        """
        
        # Nodes will be added to both queue and lis, but they will get 
        # eliminated from queue when printed while remaining in lis
        queue = []
        lis = []
        queue.append(self.root)
        while len(queue) > 0:
            a = queue.pop()
            if a not in lis:
                lis.append(a)
            s = ""
            if a.IS_LEAF: 
                s += "Leaf " 
            else: 
                s += "Internal "
            s += "Node: "
            for i in range(a.size+1):
                if a.pointers[i] != None:
                    if a.pointers[i] not in lis:
                        # Appends nodes in pointers to queue if they
                        # have not been printed yet
                        queue.append(a.pointers[i])
                    s += " ("+str(a.pointers[i].keys)+") "
                else:
                    s += " ("+str(a.pointers[i])+") "
                if i < a.size:
                    s += str(a.keys[i])
            print(s)
	
    def insert(self, x: int) -> None:
        """
        Inserts input data into the tree as a leaf node.
        
        Parameters:
            x (int): Input data.
        """
        
        # If root is None then assign a new node with the input
        # data as root
        if self.root == None:
            self.root = Node()
            self.root.keys[0] = x
            self.root.IS_LEAF = True
            self.root.size = 1
        else:
            # Traverse the tree until reaching the leaf nodes
            n = self.root
            parent = None
            while not n.IS_LEAF:
                parent = n
                # Iterate through keys in node
                for i in range(n.size):
                    if n.keys[i] != None:
                        # It found the position for insertion
                        if x < n.keys[i]:
                            n = n.pointers[i]
                            break
                    if i == n.size-1:
                        # If reached the end so it moves onto the pointers
                        # to the right of the keys
                        n = n.pointers[i+1]
                        break
                    
            if n.size < MAX:
                # Node has not reached MAX size
                
                # Finds position for insertion
                i = 0
                while i<n.size and x>n.keys[i]:
                    i += 1
                
                # Moves keys according to the placement x will have 
                # among them
                for j in range(n.size, i, -1):
                    n.keys[j] = n.keys[j-1]
                
                # Inserts x into keys
                n.keys[i] = x
                n.size += 1
                n.pointers[n.size] = n.pointers[n.size-1]
                n.pointers[n.size-1] = None
                
            else:
                
                # Node has reached MAX size
                
				# Creates a new leaf node
                leaf = Node()
                aux_node = [None]*(MAX+1)

				# Copies n's key data onto aux_node
                for i in range(MAX):
                    aux_node[i] = n.keys[i]
				
                # Finds position for insertion
                i = 0
                while i<MAX and x>aux_node[i]:
                    i += 1
                
                # Moves aux_node keys according to the placement x
                # will have among them
                for j in range(MAX, i, -1) :
                    aux_node[j] = aux_node[j-1]

                # Inserts x into aux_node keys
                aux_node[i] = x
                n.size = int((MAX+1) / 2)
                leaf.size = round(MAX+1 - (MAX+1)/2)
                n.pointers[n.size] = leaf
                leaf.pointers[leaf.size] = n.pointers[MAX]
                n.pointers[MAX] = None
                leaf.IS_LEAF = True
                
				# Updates aux_node keys to previous ones
                for i in range(n.size):
                    n.keys[i] = aux_node[i]
                n.keys[n.size] = None
				
				# Updates the leaf keys to aux_node
                j = n.size
                for i in range(leaf.size):
                    leaf.keys[i] = aux_node[j]
                    j += 1
				
                if n == self.root:
                    # The root will be modified
                    
                    # Creates a new root node
                    new_root = Node()

					# Updates new root's data
                    new_root.keys[0] = leaf.keys[0]
                    new_root.pointers[0] = n
                    new_root.pointers[1] = leaf
                    new_root.IS_LEAF = False
                    new_root.size = 1
                    self.root = new_root
                else:
                    self.insertInternal(leaf.keys[0], parent, leaf)
 
    def insertInternal(self, x: int, cursor: Node, child: Node) -> None:
        """
        Inserts input data x into cursor keys and adds child to its children.
        
        Child will be added to the right of where the new key x is inserted.        
        Parameters:
            x (int): Input data.
            cursor (Node): Node where x will be inserted.
            child (Node): Node cursor will point to.
        """
        
        if cursor.size < MAX:
            # cursor size has not reached MAX
            
            # Finds position for insertion among cursor keys
            i = 0
            while i < cursor.size:
                if cursor.keys[i] != None:
                    if x > cursor.keys[i]:
                        i += 1
                    else:
                        break         

            # Moves cursor keys to make space for the insertion
            # of x
            for j in range(cursor.size, i, -1) :
                cursor.keys[j] = cursor.keys[j-1]
            
            # Traverse the cursor node
            # and update the current pointers
            # to its previous node pointers
            for j in range(cursor.size+1, i+1, -1):
                cursor.pointers[j] = cursor.pointers[j-1]
            
            cursor.keys[i] = x
            cursor.size += 1
            cursor.pointers[i+1] = child
            
            # Checks for repeated keys
            if cursor.pointers[i]!=None and i<cursor.size:
                if (cursor.pointers[i].keys[cursor.pointers[i].size] == cursor.pointers[i+1].keys[0]
                    or cursor.pointers[i].keys[cursor.pointers[i].size] == cursor.keys[i]):
                    cursor.pointers[i].keys[cursor.pointers[i].size] = None

        else:
            # cursor size has reached MAX
            
            new_internal = Node()
            aux_key = [None]*(MAX+1)
            aux_pointer = [None]*(MAX+2)

            # Inserts keys of cursor node to aux_key
            for i in range(MAX):
                aux_key[i] = cursor.keys[i]
            
            # Inserts pointers of cursor node to aux_pointer
            for i in range(MAX+1):
                aux_pointer[i] = cursor.pointers[i]

            # Find where the new node is to be inserted
            i = 0
            while i < MAX:
                if x > aux_key[i]:
                    i += 1
                else:
                    break

            # Changes each element in aux_key to the one on its left
            for j in range(MAX, i, -1):
                aux_key[j] = aux_key[j-1]
            
            aux_key[i] = x

            # Changes each element in aux_pointer to the one on its left
            for j in range(MAX+1, i+1, -1):
                aux_pointer[j] = aux_pointer[j-1]
            
            # Adds child to aux_pointer
            aux_pointer[i+1] = child
            
            new_internal.IS_LEAF = False
            cursor.size = int((MAX+1) / 2)
            new_internal.size = round(MAX - (MAX)/2)#round(MAX - (MAX+1)/2)
            
            # Inserts new node as an internal node
            j = cursor.size + 1
            for m in range(new_internal.size):
                new_internal.keys[m] = aux_key[j]
                j += 1
            
            j = cursor.size + 1
            for m in range(new_internal.size+1):
                new_internal.pointers[m] = aux_pointer[j]
                j += 1
            
            # Checks for repeated keys
            for i in range(new_internal.size):
                if new_internal.pointers[i]!=None and i<new_internal.size:
                    if (new_internal.pointers[i].keys[new_internal.size] == new_internal.pointers[i+1].keys[0] 
                        or new_internal.pointers[i].keys[new_internal.size] == new_internal.keys[i]):
                        new_internal.pointers[i].keys[new_internal.size] = None
            
            if cursor == self.root:
                # cursor is root
                
                # Creates new node for root
                new_root = Node()
                
                # Update new root's keys value
                new_root.keys[0] = cursor.keys[cursor.size]
                
                # Sets overflow cursor keys and pointers to None
                for i in range(cursor.size, MAX):
                    cursor.keys[i] = None
                    cursor.pointers[i+1] = None
                
                # Makes new root's singular key point to the left 
                # to cursor and to the right to new_internal
                new_root.pointers[0] = cursor
                new_root.pointers[1] = new_internal
                
                new_root.IS_LEAF = False
                new_root.size = 1
                self.root = new_root

            else:
                # cursor is not root
                
                for i in range(MAX):
                    if i < cursor.size:
                        cursor.keys[i] = aux_key[i]
                    else:
                        if aux_key[cursor.size] in cursor.pointers[i].keys:
                            cursor.pointers[i] = child
                        cursor.pointers[i+1] = None
                
                self.insertInternal(aux_key[cursor.size], self.findParent(self.root, cursor), new_internal)
	
    def findParent(self, cursor: Node, child: Node) -> Node|None:
        """
        Finds and returns parent node of input child.
        
        Calls itself recursively traversing the cursor's children
        until the input cursor is the parent of child.
        
        Parameters:
            cursor (Node): Node to be verified as parent to child.
            child (Node): Input child.
            
        Returns:
            Node: Parent of input child.
        """
		# If cursor reaches the end of tree
        if cursor.IS_LEAF or (cursor.pointers[0]).IS_LEAF:
            return None
		
		# Traverses the current node with
		# all its children
        for i in range(cursor.size+1):
            if cursor.pointers[i] == child:
                # Cursor points to child, so it is its parent
                parent = cursor
                return parent
            else:
                # Recursively traverses to find child node
                parent = self.findParent(cursor.pointers[i], child)

				# If parent is found, then
				# return that parent node
                if (parent != None):
                    return parent
		
		# Return parent node
        return parent