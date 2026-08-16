import os
import json
import nbformat
from pathlib import Path
from google import genai

# --------------------------
# CONFIGURATION
# --------------------------

PROMPT_TEMPLATE_PATH = Path("Track_Trace_Enhancement_Prompt.txt")  # Enhanced prompt file
if not PROMPT_TEMPLATE_PATH.exists():
    raise FileNotFoundError("❌ Missing enhanced prompt file: Track_Trace_Enhancement_Prompt.txt")

PROMPT_TEMPLATE = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")

# Initialize GenAI client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# --------------------------
# UTILITY FUNCTIONS
# --------------------------

def extract_code_from_notebook(notebook_path):
    """Extract all code cells from a Jupyter Notebook as plain text."""
    try:
        nb = nbformat.read(open(notebook_path, encoding="utf-8"), as_version=4)
        code_cells = [
            cell["source"]
            for cell in nb.cells
            if cell["cell_type"] == "code" and cell["source"].strip()
        ]
        return "\n\n".join(code_cells)
    except Exception as e:
        print(f"⚠️ Could not read {notebook_path.name}: {e}")
        return ""


def collect_notebook_code(notebooks_folder):
    """Combine all code from notebooks in the specified folder."""
    notebooks_folder = Path(notebooks_folder)
    if not notebooks_folder.exists():
        raise FileNotFoundError(f"❌ Notebooks folder not found: {notebooks_folder}")

    all_code_snippets = []
    for nb_file in notebooks_folder.glob("*.ipynb"):
        print(f"💾 Reading code from: {nb_file.name}")
        code = extract_code_from_notebook(nb_file)
        if code:
            all_code_snippets.append(code)

    combined_code = "\n\n".join(all_code_snippets)
    if not combined_code:
        print("⚠️ No valid code found in notebooks.")
    return combined_code


# --------------------------
# MAIN FUNCTION
# --------------------------

def enhance_markdowns_with_notebooks(markdown_folder, notebooks_folder):
    """
    Enhance Markdown Codebooks using the enhanced prompt and Python code from notebooks.
    - markdown_folder: folder containing .md Codebooks
    - notebooks_folder: folder containing .ipynb notebooks
    """
    markdown_folder = Path(markdown_folder)
    if not markdown_folder.exists():
        raise FileNotFoundError(f"❌ Markdown folder not found: {markdown_folder}")

    output_folder = markdown_folder / "enhanced_codebooks"
    output_folder.mkdir(exist_ok=True)

    markdown_files = list(markdown_folder.glob("*.txt"))
    if not markdown_files:
        print("⚠️ No Markdown files found.")
        return

    # Collect all code from notebooks
    combined_code = collect_notebook_code(notebooks_folder)

    # Process each markdown
    for md_file in markdown_files:
        print(f"📘 Enhancing: {md_file.name}")

        md_content = md_file.read_text(encoding="utf-8")

        # Construct the full prompt
        full_prompt = (
            f"{PROMPT_TEMPLATE}\n\n"
            f"---\n\n"
            f"CODEBOOK MARKDOWN:\n{md_content}\n\n"
            f"---\n\n"
            f"PYTHON CODE SNIPPETS:\n{combined_code}"
        )

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt,
                config={"temperature": 0.2}
            )

            output_path = output_folder / f"{md_file.stem}_enhanced.md"
            output_path.write_text(response.text, encoding="utf-8")

            print(f"✅ Saved enhanced file: {output_path.name}")

        except Exception as e:
            print(f"❌ Error processing {md_file.name}: {e}")

    print(f"\n🎉 All enhanced Markdown files saved in: {output_folder}")


# --------------------------
# USAGE EXAMPLE
# --------------------------
# Example folders:
markdown_folder = "Distribution_codebooks"
notebooks_folder = "Notebooks"

enhance_markdowns_with_notebooks(markdown_folder, notebooks_folder)
