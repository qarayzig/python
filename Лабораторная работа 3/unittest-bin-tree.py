import unittest
from LR-3 import gen_bin_tree
class TestGenBinTree(unittest.TestCase):
    
    def test_height_1(self):
        result = gen_bin_tree(height=1, root=5)
        self.assertEqual(result, 5)

    def test_default_tree(self):
        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 5)
        self.assertEqual(tree["left"]["value"], )
        self.assertEqual(tree["right"]["value"], 3)

    def test_custom_functions(self):
        tree = gen_bin_tree(height=3, root=2,
                            left_leaf=lambda x: x-2,
                            right_leaf=lambda x: x**2)
        self.assertEqual(tree["value"], 2)
        self.assertEqual(tree["left"]["value"], 3)
        self.assertEqual(tree["right"]["value"], 4)
        self.assertEqual(tree["left"]["left"], 4)
        self.assertEqual(tree["left"]["right"], 6)

if __name__ == "__main__":
    unittest.main()