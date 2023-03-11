class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorden(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorden(node.left)
    preorden(node.right)

def posorden(node):
    if node is None:
        return
    posorden(node.left)
    posorden(node.right)
    print(node.value, end=" ")

def inorden(node):
    if node is None:
        return
    inorden(node.left)
    print(node.value, end=" ")
    inorden(node.right)  

#Se Crea el arbol
root = Node('A')
root.left = Node('B')
root.right = Node('C') 
root.left.left = Node('D')
root.left.right = Node('E')
root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.left.right.right = Node('K')
root.right.left = Node('F')
root.right.left.left = Node('L')
root.right.left.right = Node('M')
root.right.right = Node('G')
root.right.right.left = Node('N')
root.right.right.right = Node('Fin')       

print("\nRecorrido Preorden")
preorden(root)

print("\nRecorrido Posotden")
posorden(root)

print("\nRecorrido Inorden")
inorden(root)