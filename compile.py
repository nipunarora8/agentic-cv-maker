import subprocess
import os
import argparse
import shutil

def convert_tex_to_pdf(tex_file_path, output_pdf_path=None, engine='xelatex'):
    engine_path = f'/Library/TeX/texbin/{engine}'
    
    if not os.path.exists(tex_file_path):
        print(f"Error: The file '{tex_file_path}' does not exist.")
        return

    # Determine where the files should be built
    # If no output path is provided, we use the directory of the input file
    target_dir = os.path.dirname(output_pdf_path) if output_pdf_path else os.path.dirname(tex_file_path)
    if not target_dir:
        target_dir = '.' # Fallback to current directory
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        print(f"Compiling '{tex_file_path}' using {engine}...")
        # Added -output-directory to the command
        subprocess.run(
            [engine_path, '-interaction=nonstopmode', f'-output-directory={target_dir}', tex_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print("Compilation successful!")
        
    except subprocess.CalledProcessError as e:
        print("An error occurred during compilation.")
        print(e.stdout)
        return

    # --- Cleanup and Renaming ---
    # The engine creates the PDF with the same name as the .tex file in the target_dir
    input_filename_base = os.path.splitext(os.path.basename(tex_file_path))[0]
    generated_pdf = os.path.join(target_dir, input_filename_base + '.pdf')

    # 1. Handle Rename if specific output name was requested
    if output_pdf_path and generated_pdf != output_pdf_path:
        shutil.move(generated_pdf, output_pdf_path)
        final_path = output_pdf_path
    else:
        final_path = generated_pdf

    # 2. Cleanup auxiliary files in the target_dir
    extensions_to_remove = ['.aux', '.log', '.out', '.toc', '.fls', '.synctex.gz']
    for ext in extensions_to_remove:
        file_to_remove = os.path.join(target_dir, input_filename_base + ext)
        if os.path.exists(file_to_remove):
            os.remove(file_to_remove)

    print(f"Done! PDF saved to: {final_path}")
if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Compile a LaTeX file into a PDF and clean up auxiliary files.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input .tex file")
    parser.add_argument('-o', '--output', required=False, help="Path to the output .pdf file (optional)")
    parser.add_argument('-e', '--engine', default='xelatex', choices=['pdflatex', 'xelatex', 'lualatex'], help="LaTeX engine to use (default: xelatex)")
    
    args = parser.parse_args()
    
    # Run the function with the provided arguments
    convert_tex_to_pdf(args.input, args.output, args.engine)