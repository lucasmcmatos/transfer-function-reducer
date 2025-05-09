from sympy import Expr, sympify

class Block:
    """
    Represents a block with a name and a symbolic transfer function.
    """

    def __init__(self, name: str, transfer_function: Expr):
        self.name = name
        self.transfer_function = transfer_function

    @classmethod
    def from_string(cls, name:str, expr_str: str) -> 'Block':
        """
        Create a Block fro a string expression.

        Args:
            name (str): Block identifier.
            expr_str (str): Transfer function in symbolic string form.

        Returns:
            Block: New Block instance with aprsed transfer function.
        """

        tf = sympify(expr_str)
        return cls(name, tf)