#DFS Traversals of tree are 3 types
# PreOrder, InOrder, PostOrder

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.righ)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root):
    if not root:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
    
