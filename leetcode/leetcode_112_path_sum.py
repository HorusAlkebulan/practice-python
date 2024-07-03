from typing import Optional

from leetcode.test_leetcode_112_path_sum import TreeNode

def print_binary_tree(tree: TreeNode):
    print(binary_tree_text(tree))

def binary_tree_text(tree: TreeNode) -> str:
    if tree is None:
        return '_'
    
    output = '['
    output += '[' + binary_tree_text(tree.left) + ']'
    output += str(tree.val)
    output += '[' + binary_tree_text(tree.right) + ']'
    output += ']'
    return output

# Example usage:
# root = to_binary_tree([3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])


# if __name__ == "__main__":
#     test_hasPathSum_example_1()
#     test_hasPathSum_example_2()
#     test_hasPathSum_example_3()
