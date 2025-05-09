# Transfer Function Reducer (Block Diagram Reducer)

## Overview

**BlockReducer** is a Python library and command-line tool that automatically reduces control-engineering block diagrams into a single, simplified transfer function. Given a JSON representation of blocks and their interconnections, it applies series, parallel, and feedback reductions in sequence and outputs the final symbolic expression.

## Features

* **JSON-based input**: Define blocks and connections in an easy-to-read JSON format.
* **Symbolic manipulation**: Uses [SymPy](https://www.sympy.org/) for algebraic simplification.
* **Support for all standard connections**: Series, parallel, and feedback loops.
* **Iterative reduction**: Continues simplifying until only one transfer function remains.
* **Example library**: Includes sample JSON files for series, parallel, feedback, and complex diagrams.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/block-reducer.git
   cd block-reducer
   ```
2. **Create and activate a virtual environment** (recommended)

   * On **Linux/macOS**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * On **Windows**:

     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The main script is `main.py`. Edit the `file_path` variable to point to one of the example JSON files or your own diagram file.

```bash
python main.py
```

By default, it reads from `examples/diagram.json`. To test a different example, open `main.py` and change:

```python
file_path = 'examples/diagram.json'
```

to:

```python
file_path = 'examples/complex.json'
```

Then run:

```bash
python main.py
```

The final reduced transfer function will be printed to the console.

### Sample Output

```bash
$ python main.py
Reduced transfer function: 10/(s + 1)
```

## Project Structure

```plaintext
block_reducer/
├── input/
│   └── parser.py       # JSON loader and validator
├── model/
│   ├── block.py        # Block class with symbolic transfer function
│   └── diagram.py      # Diagram loader from dict
├── operations/
│   ├── series.py       # Series reduction logic
│   ├── parallel.py     # Parallel reduction logic
│   └── feedback.py     # Feedback loop reduction logic
├── reduction/
│   └── reducer.py      # Iterative reduction engine
├── output/
│   └── display.py      # Console display of results
├── examples/           # JSON input samples
│   ├── series.json
│   ├── parallel.json
│   ├── feedback.json
│   └── complex.json
├── requirements.txt    # Project dependencies
└── main.py             # Application entry point
```

## Requirements

* **Python 3.7+**
* **SymPy** for symbolic mathematics

Install SymPy manually if not using `requirements.txt`:

```bash
pip install sympy
```

## Contributing

Contributions, issues, and feature requests are welcome! Please:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

