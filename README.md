# Woff Wrangler

Woff Wrangler is a Python tool for converting WOFF and WOFF2 font files to OTF format.

## Features

- Convert single WOFF or WOFF2 files to OTF
- Batch convert all WOFF and WOFF2 files in a directory
- Simple command-line interface

## Installation

1. Ensure you have Python 3.6 or later installed.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/woff-wrangler.git
   cd woff-wrangler
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To convert a single file:
```
python woff_wrangler.py input.woff -o output.otf
```

To convert all WOFF and WOFF2 files in a directory:
```
python woff_wrangler.py input_directory -o output_directory
```

If no output is specified, the converted file(s) will be placed in the same directory as the input.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.