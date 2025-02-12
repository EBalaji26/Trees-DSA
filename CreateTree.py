class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def CreateTree():
    x = int(input("Enter data [enter -1 to stop]"))
    if x == -1:
        return
    temp = Node(x)
    print("Enter left Node of ", x)
    temp.left = CreateTree()
    print("Enter right Node of ", x)
    temp.right = CreateTree()
    
    return temp

#for creating a tree just call CreateTree() which returns the root.
#root = CreateTree()


            
