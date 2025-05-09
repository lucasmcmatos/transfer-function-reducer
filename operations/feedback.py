from sympy import Expr

def reduce_feedback(forward: Expr, feedback: Expr) -> Expr:
    """
    Reduce a feedback loob: G = forward / (1 + forward * feedback)

    Args:
        forward (Expr): Transfer function of the first block.
        feedback (Expr): Transfer fucntion of the second block.

    Returns:
        Expr: Closed-loop tranfer function.
    """

    return forward / (1 + forward * feedback)