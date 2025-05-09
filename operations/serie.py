from sympy import Expr

def reduce_series(a: Expr, b: Expr) -> Expr:
    """
    Reduce two blocks inseries: G = a * b.

    Args:
        a (Expr): Transfer function of the first block.
        b (Expr): Transfer function of the second block.

    Returns:
        Expr: Combined transfer function in series.
    """

    return a * b