import subprocess
import os
import argparse
import shutil

def convert_tex_to_pdf(tex_file_path, output_pdf_path=None, engine='pdflatex'):
    # Standard installation path for pdflatex on macOS
    engine_path = f'/Library/TeX/texbin/{engine}'
    
    if not os.path.exists(tex_file_path):
        print(f"Error: The file '{tex_file_path}' does not exist.")
        return

    try:
        print(f"Compiling '{tex_file_path}' using {engine}...")
        # Compile the tex file
        subprocess.run(
            [engine_path, '-interaction=nonstopmode', tex_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print("Compilation successful!")
        
    except subprocess.CalledProcessError as e:
        print("An error occurred during compilation.")
        print(e.stdout)
    except FileNotFoundError:
        print(f"Error: Could not find {engine} at {engine_path}.")
        print("Please ensure MacTeX is installed.")
        return 

    # --- Cleanup Auxiliary Files ---
    print("Cleaning up auxiliary files...")
    base_name = os.path.splitext(tex_file_path)[0] 
    extensions_to_remove = ['.aux', '.log', '.out', '.toc', '.fls', '.synctex.gz']
    
    for ext in extensions_to_remove:
        file_to_remove = base_name + ext
        if os.path.exists(file_to_remove):
            try:
                os.remove(file_to_remove)
            except OSError as e:
                print(f"Warning: Could not remove {file_to_remove}. Reason: {e}")

    # --- Handle Output Renaming/Moving ---
    default_pdf_path = base_name + '.pdf'
    
    # If the user specified an output path and the PDF was generated successfully
    if output_pdf_path and os.path.exists(default_pdf_path):
        # Extract the directory part of the requested output path
        out_dir = os.path.dirname(output_pdf_path)
        
        # Create the target directory if it doesn't exist
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir)
            
        # Move and rename the generated PDF
        shutil.move(default_pdf_path, output_pdf_path)
        print(f"Done! PDF saved to: {output_pdf_path}")
        
    elif os.path.exists(default_pdf_path):
        # If no output path was specified, leave it where it is
        print(f"Done! PDF saved to: {default_pdf_path}")
    else:
        print("Error: PDF was not generated. Please check your LaTeX syntax.")

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Compile a LaTeX file into a PDF and clean up auxiliary files.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input .tex file")
    parser.add_argument('-o', '--output', required=False, help="Path to the output .pdf file (optional)")
    parser.add_argument('-e', '--engine', default='pdflatex', choices=['pdflatex', 'xelatex', 'lualatex'], help="LaTeX engine to use (default: pdflatex)")
    
    args = parser.parse_args()
    
    # Run the function with the provided arguments
    convert_tex_to_pdf(args.input, args.output, args.engine)