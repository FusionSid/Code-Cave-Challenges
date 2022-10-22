Given the root of a binary tree, invert the tree, and return its root.

Example 1:
```py
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
Example 2:
```py
Input: root = [2,1,3]
Output: [2,3,1]
```
Example 3:
```py
Input: root = []
Output: []
 ```

```py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Visualised:  
This:
```
                1
              /    \
            2        3
          /   \    /   \
        4      5  6     7
```
Becomes:
```
                1
              /    \
            3        2
          /   \    /   \
        7      6  5     4
```