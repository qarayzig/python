from typing import Callable, Union, Dict

def gen_bin_tree(
    height: int = 6,
    root: int = 5,
    left_leaf: Callable[[int], int] = lambda x: x ** 2,
    right_leaf: Callable[[int], int] = lambda y: y - 2
) -> Dict[str, Union[int, dict, None]]:
    """
    Генерирует бинарное дерево заданной высоты с пользовательскими функциями для
    левого и правого потомка.

    Аргументы:
        height (int): Высота дерева. Минимальное значение = 1.
        root (int): Значение корневого узла.
        left_leaf (Callable[[int], int]): Функция для вычисления значения левого потомка.
        right_leaf (Callable[[int], int]): Функция для вычисления значения правого потомка.

    Возвращает:
        Dict[str, Union[int, dict, None]]: Словарь, представляющий дерево.
        Ключи: 'value', 'left', 'right'. Листовые узлы имеют 'left' и 'right' = None.
    """
    if height == 1:
        return {"value": root, "left": None, "right": None}
    
    left_value = left_leaf(root)
    right_value = right_leaf(root)
    
    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_value, left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_value, left_leaf, right_leaf)
    }
