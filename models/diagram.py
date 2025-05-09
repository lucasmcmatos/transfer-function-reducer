from typing import List, Dict
from .block import Block

class Diagram:
    """
    Represents collection of blocks and their connections.
    """

    def __init__(self, blocks: List[Block], connections: List[Dict]):  # Possível erro !
        self.blocks = blocks
        self.connections = connections

    @classmethod
    def from_dict(cls, data: Dict) -> 'Diagram':
        """
        Create a Diagram from a data dictionary.

        Args:
            data (dict): Dictionary with 'blocks' and 'connections'.

        Returns:
            Diagram: New Diagram instance.
        """

        blocks = [Block.from_string(name, expr) for name, expr in data['blocks'].items()]
        connections = data['connections']
        return cls(blocks, connections)
        