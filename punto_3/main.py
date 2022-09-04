from b_plus_tree import BPlusTree

# Create B+ Tree
tree = BPlusTree()
print("\nNOTE:\n1. Nodes will be printed following the format: "
      + "\n\"Leaf/Internal Node: (pointers[0]) keys[0] "
      + "(pointers[1]) keys[1] ... keys[node.size] "
      + "(pointers[node.size+1])\"\n2. The first node for every "
      + "printed tree will be its root.\n")
            
# Fill B+ Tree by reading through file
with open(file='datos.csv', encoding='utf-8') as f:
      while (line:=f.readline()) != '':
            line = line.removesuffix('\n').split(';', 1)
            print("\nTree after inserting " + line[0] + ":")
            # Insert ID to tree
            try:
                  tree.insert(int(line[0]))
            except:
                  tree.insert(int(line[0][1:]))
            tree.print_tree() # Print tree