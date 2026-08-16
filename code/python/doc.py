import pypandoc
from pathlib import Path

def convert_md_to_docx(input_md_path, output_docx_path=None):
    """
    Converts a Markdown file to a Word (.docx) document.
    Maintains headings, tables, and formatting.
    """
    input_path = Path(input_md_path)
    if not input_path.exists():
        raise FileNotFoundError(f"❌ Markdown file not found: {input_md_path}")

    # Default output name if not provided
    if output_docx_path is None:
        output_docx_path = input_path.with_suffix(".docx")

    print(f"🧾 Converting '{input_path.name}' → '{Path(output_docx_path).name}' ...")

    # Convert Markdown → DOCX using Pandoc
    pypandoc.convert_text(
        input_path.read_text(encoding="utf-8"),
        to="docx",
        format="md",
        outputfile=str(output_docx_path),
        extra_args=["--standalone"]
    )

    print(f"✅ Conversion complete: {output_docx_path}")
    return output_docx_path


# --------------------------------------------
# Example Usage
# --------------------------------------------
if __name__ == "__main__":
    # Update this path to your combined codebook markdown file
    convert_md_to_docx("enhanced_codebooks/combined_codebook.md")
