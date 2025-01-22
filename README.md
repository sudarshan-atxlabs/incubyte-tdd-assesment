# String Calculator with TDD and Clean Code Practices

This project implements a **String Calculator** using **Test-Driven Development (TDD)** and clean code principles. It demonstrates advanced Python techniques, including logging, unit testing, and modular design.

## Features

- Supports default delimiters (`,` and `\n`).
- Allows custom delimiters (e.g., `//;\n1;2;3`).
- Handles empty input (returns `0`).
- Logs operations for debugging.
- Provides robust error handling for invalid inputs.

## Code Highlights

### StringCalculator Class

- **`add(numbers: str) -> int`**: Adds numbers from a string.
- **`_extract_custom_delimiter(numbers: str) -> Tuple[str, str]`**: Extracts custom delimiters.
- **`_split_numbers(numbers: str, delimiters: List[str]) -> List[str]`**: Splits numbers by delimiters.
- **`_to_int(number: str) -> int`**: Converts a string to an integer, raising errors for invalid values.

### TDD Practices

1. Write failing tests for each feature.
2. Write minimal code to pass the test.
3. Refactor the code while ensuring tests pass.

### Clean Code Practices

- **Readable Code**: Descriptive function names and modular design.
- **Comments**: Clear docstrings for all functions.
- **Logging**: Tracks execution flow and errors.
- **Type Annotations**: Improves code clarity and tooling support.

## How to Run

1. Clone this repository.
2. Run the tests using:
   ```bash
   python -m unittest discover
   ```

## Example Usage

```python
calculator = StringCalculator()
result = calculator.add("//;\n1;2;3")  # Returns 6
print(result)
```

## Author

Sudarshan
