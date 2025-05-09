import json

def load_diagram(file_path: str) -> dict:
    """
    Load and returns the blocks diagram from a JSON file.

    Args:
        file_path (str): Path to JSON file with keys 'blocks'
        (dict) and 'connections' (list).
    
    Returns:
        data (dict): Dictionary containing 'blocks' and 'connections'.
    """

    with open(file_path, 'r') as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Error! JSON content must be an object.")
    
    if 'blocks' not in data or 'connections' not in data:
        raise KeyError("Invalid JSON! Keys 'blocks' and 'connections' are required.")
    
    if not isinstance(data['blocks'], dict):
        raise TypeError("Blocks Type Error! 'blocks', must be a dict mapping names to transfer function strings.")
    
    if not isinstance(data['connections'], list):
        raise TypeError("Connections Type Error! 'connections', must be a list of connections definitions.")
    
    return data