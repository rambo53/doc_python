from composite import * 
 
tree = Node()

branch1 = Node()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Node()
branch2.add(Leaf())
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)


print(tree.operation())

 