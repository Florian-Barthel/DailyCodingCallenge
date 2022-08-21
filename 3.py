import json

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

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


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(input_node: Node):
    return json.dumps(serialize_recursive(input_node))


def serialize_recursive(input_node: Node):
    if input_node is None:
        return None
    result_dict = {
        'val': input_node.val,
        'left': serialize_recursive(input_node.left),
        'right': serialize_recursive(input_node.right)
    }
    return result_dict


def deserialize(description: str):
    node_dict = json.loads(description)
    return deserialize_recursive(node_dict)


def deserialize_recursive(node_dict: dict):
    if not node_dict:
        return None
    root_node = Node(
        node_dict['val'],
        left=deserialize_recursive(node_dict['left']),
        right=deserialize_recursive(node_dict['right'])
    )
    return root_node


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
