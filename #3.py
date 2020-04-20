"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import json
string_tree = ''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serelize(root):
	global string_tree  
	if not root:
		return None

	string_tree =  ' '.join([string_tree, root.val])
	
	if root.left != None : 
		serelize(root.left)
	if root.right != None : 
		serelize(root.right)
	return string_tree


node = Node('root', Node('left', Node('left.left')), Node('right'))

print(serelize(node))