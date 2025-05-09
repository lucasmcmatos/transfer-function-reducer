from sympy import Expr
from models.diagram import Diagram
from operations.serie import reduce_series
from operations.parallel import reduce_parallel
from operations.feedback import reduce_feedback 

def reduce_diagram(diagram: Diagram) -> Expr:
    """
    Iteratively apply reduction operations until a single block remains.

    Args:
        diagram (Diagram): Diagram instance with blocks and connections

    Returns:
        Expr: Simplified transfer function of the entire diagram
    """
    # Map block names to their transfer functions
    expr_map = {blk.name: blk.transfer_function for blk in diagram.blocks}
    connections = list(diagram.connections)  # cópia mutável

    def replace_references(old: str, new: str):
        for conn in connections:
            if conn.get('type') in ('series', 'parallel'):
                conn['blocks'] = [new if b == old else b for b in conn['blocks']]
            elif conn.get('type') == 'feedback':
                if conn['forward'] == old:
                    conn['forward'] = new
                if conn['feedback'] == old:
                    conn['feedback'] = new

    while connections:
        conn = connections.pop(0)
        ctype = conn.get('type')

        if ctype == 'series':
            b1, b2 = conn['blocks']
            new_expr = reduce_series(expr_map[b1], expr_map[b2])
            new_name = f"({b1}_s_{b2})"
            expr_map[new_name] = new_expr
            # delete both blocos antigos
            del expr_map[b1], expr_map[b2]
            replace_references(b1, new_name)
            replace_references(b2, new_name)

        elif ctype == 'parallel':
            b1, b2 = conn['blocks']
            new_expr = reduce_parallel(expr_map[b1], expr_map[b2])
            new_name = f"({b1}_p_{b2})"
            expr_map[new_name] = new_expr
            del expr_map[b1], expr_map[b2]
            replace_references(b1, new_name)
            replace_references(b2, new_name)

        elif ctype == 'feedback':
            fwd = conn['forward']
            fb  = conn['feedback']
            new_expr = reduce_feedback(expr_map[fwd], expr_map[fb])
            new_name = f"({fwd}_f_{fb})"
            expr_map[new_name] = new_expr
            # apaga cada bloco apenas uma vez
            for key in {fwd, fb}:
                del expr_map[key]
            replace_references(fwd, new_name)
            replace_references(fb, new_name)

        else:
            raise ValueError(f"Unknown connection type: {ctype}")

    # ao final deve restar exatamente uma função de transferência
    if len(expr_map) != 1:
        raise ValueError("Reduction incomplete: multiple blocks remain.")
    return next(iter(expr_map.values()))
