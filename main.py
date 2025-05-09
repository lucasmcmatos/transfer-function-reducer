from input.parser import load_diagram
from models.diagram import Diagram
from reduction.reducer import reduce_diagram
from output.display import display_result

def main():
    """
    Main entry oint for the block reducer application.
    """

    file_path = 'examples/series.json'
    data = load_diagram(file_path)
    diagram = Diagram.from_dict(data)
    final_tf = reduce_diagram(diagram)
    display_result(final_tf)

if __name__ == '__main__':
    main()