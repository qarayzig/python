import unittest
from LR_3 import gen_bin_tree

class TestGenBinTree(unittest.TestCase):

    def test_height_1(self):
        """Тест для дерева высотой 1 (должен вернуться листовой узел)"""
        result = gen_bin_tree(height=1, root=5)
        expected = {"value": 5, "left": None, "right": None}
        self.assertEqual(result, expected)

    def test_default_tree(self):
        """Тест дерева с параметрами по умолчанию"""
        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 5)          # корень
        self.assertEqual(tree["left"]["value"], 25) # левый потомок
        self.assertEqual(tree["right"]["value"], 3) # правый потомок

    def test_custom_functions(self):
        """Тест дерева с пользовательскими функциями для потомков"""
        tree = gen_bin_tree(height=3, root=2,
                            left_leaf=lambda x: x+1,
                            right_leaf=lambda x: x*2)
        # Проверка корня
        self.assertEqual(tree["value"], 2)
        self.assertEqual(tree["left"]["value"], 3)  # 2 + 1
        self.assertEqual(tree["right"]["value"], 4) # 2 * 2
        # Проверка третьего уровня
        self.assertEqual(tree["left"]["left"]["value"], 4)  # 3 + 1
        self.assertEqual(tree["left"]["right"]["value"], 6) # 3 * 2
        self.assertEqual(tree["right"]["left"]["value"], 5) # 4 + 1
        self.assertEqual(tree["right"]["right"]["value"], 8)# 4 * 2
        # Листовые узлы должны иметь left=None и right=None
        self.assertIsNone(tree["left"]["left"]["left"])
        self.assertIsNone(tree["left"]["left"]["right"])
        self.assertIsNone(tree["right"]["right"]["left"])
        self.assertIsNone(tree["right"]["right"]["right"])

if __name__ == "__main__":
    unittest.main()
