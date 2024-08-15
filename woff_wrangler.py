#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
from fontTools.ttLib import TTFont

def convert_to_otf(input_path: Path, output_path: Path) -> None:
    """
    Convert WOFF or WOFF2 font to OTF.

    Args:
        input_path (Path): Path to the input WOFF or WOFF2 file.
        output_path (Path): Path to save the output OTF file.
    """
    try:
        # Open the font file
        font = TTFont(input_path)
        
        # Remove WOFF-specific metadata
        for table_tag in ['WOFF', 'wOFF', 'wOF2']:
            if table_tag in font:
                del font[table_tag]
        
        # Ensure the font is saved as OTF
        font.flavor = None
        
        # Save as OTF
        font.save(output_path)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")

def process_directory(input_dir: Path, output_dir: Path) -> None:
    """
    Process all WOFF and WOFF2 files in the input directory.

    Args:
        input_dir (Path): Path to the input directory.
        output_dir (Path): Path to the output directory.
    """
    for file in input_dir.glob('*'):
        if file.suffix.lower() in ['.woff', '.woff2']:
            output_path = output_dir / f"{file.stem}.otf"
            convert_to_otf(file, output_path)

def main():
    parser = argparse.ArgumentParser(description="Woff Wrangler: Convert WOFF and WOFF2 fonts to OTF")
    parser.add_argument('input', help="Input WOFF/WOFF2 file or directory")
    parser.add_argument('-o', '--output', help="Output OTF file or directory (default: same as input)")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.parent

    if input_path.is_file():
        if not args.output:
            output_path = input_path.with_suffix('.otf')
        convert_to_otf(input_path, output_path)
    elif input_path.is_dir():
        if not output_path.exists():
            output_path.mkdir(parents=True)
        process_directory(input_path, output_path)
    else:
        print(f"Error: {input_path} is not a valid file or directory")

if __name__ == "__main__":
    main()