from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def path_sum(tree: Optional[TreeNode], path: list, target_sum: int) -> bool:
    # print(f'\t path_sum(tree: Optional[TreeNode]={tree}, path: list={path}, targetSum: int={target_sum})')
    # print_binary_tree(tree)
    # terminal cases

    # leaf
    if tree is None:
        return False

    # try to add current value to list, we'll remove if it doesn't pass branching
    path.append(tree.val)
    # print(f'\t\tAdding current value resulting in list to check sum: {path}')

    if tree.left is None and tree.right is None:
        if sum(path) == target_sum:
            return True
        else:
            return False

    # # branching cases
    # left_result = False
    # right_result = False

    # if tree.left is not None:
    left_result = path_sum(tree.left, path, target_sum)

    # if tree.right is not None:
    right_result = path_sum(tree.right, path, target_sum)

    if left_result or right_result:
        return True
    else:
        return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given the root of a binary tree and an integer targetSum, return true if
        the tree has a root-to-leaf path such that adding up all the values along
        the path equals targetSum.

        A leaf is a node with no children.
        """
        print(
            f"hasPathSum(self, root: Optional[TreeNode]={root}, targetSum: int={targetSum})"
        )

        if root is None:
            return False

        if root.left is None and root.right is None:
            # leaf node
            if targetSum == root.val:
                return True
            else:
                return False

        # recursive case, trying to get to zero
        sub_target_sum = targetSum - root.val
        if self.hasPathSum(root.left, sub_target_sum) or self.hasPathSum(
            root.right, sub_target_sum
        ):
            return True
        else:
            return False

    def hasPathSumWithPath(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given the root of a binary tree and an integer targetSum, return true if
        the tree has a root-to-leaf path such that adding up all the values along
        the path equals targetSum.

        A leaf is a node with no children.
        """
        print(
            f"hasPathSum(self, root: Optional[TreeNode]={root}, targetSum: int={targetSum})"
        )

        path = []
        has_path_sum = path_sum(root, path, targetSum)
        return has_path_sum


def to_binary_tree(items: list[int]) -> TreeNode:
    """
    Create a binary tree from a list of values.
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def test_hasPathSum_example_1():
    test_name = "test_hasPathSum_example_1"
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    expected_output = True

    print(f"=== {test_name} ===")
    tree = to_binary_tree(root)

    solver = Solution()
    result = solver.hasPathSum(tree, targetSum)
    assert result == expected_output


def test_hasPathSum_example_2():
    test_name = "test_hasPathSum_example_1"
    root = [1, 2, 3]
    targetSum = 5
    expected_output = False

    print(f"=== {test_name} ===")
    tree = to_binary_tree(root)

    solver = Solution()
    result = solver.hasPathSum(tree, targetSum)
    assert result == expected_output


def test_hasPathSum_example_3():
    test_name = "test_hasPathSum_example_3"
    root = []
    targetSum = 0
    expected_output = False

    print(f"=== {test_name} ===")
    tree = to_binary_tree(root)

    solver = Solution()
    result = solver.hasPathSum(tree, targetSum)
    assert result == expected_output


if __name__ == "__main__":
    test_hasPathSum_example_1()
    test_hasPathSum_example_2()
    test_hasPathSum_example_3()
