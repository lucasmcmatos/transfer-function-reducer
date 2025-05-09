from sympy import Expr

def reduce_parallel(a: Expr, b: Expr) -> Expr:
    """
    Reduce two blocks in parallel: G = a + b

    Args:
        a (Expr): Transfer function of the first block.
        b (Expr): Transfer fucntion of the second block.

    Returns:
        Expr: Combined transfer function in parallel.
    """

    return a + b