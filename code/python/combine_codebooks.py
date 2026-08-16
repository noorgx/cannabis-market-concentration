from pathlib import Path
import re
import json
import pandas as pd

# ✅ Category mapping provided
files_by_folder = {
    "Cultivation": [
        "cultpanelsize",
        "harvestpackagemerge19-24",
        "harvestpackagemerge23-24",
        "harvestpackagemerge25",
        "harvestqty19-24",
        "harvestqty23-24",
        "harvestqty25",
        "packageqty19-24",
        "packageqty23-24",
        "packageqty25"
    ],
    "Harvest": [
        "harvest"
    ],
    "Package": [
        "package"
    ],
    "Retail": [
        "sales18",
        "sales19",       
        "sales20",
        "sales21",
        "sales22",
        "sales23",
        "sales23v2",
        "sales24",
        "sales25",
        "sales25q2",     
        "salesquantity18",
        "salesquantity19",
        "salesquantity20",
        "salesquantity21",
        "salesquantity22",
        "salesquantity23",
        "salesquantity23v2",
        "salesquantity24",
        "salesquantity25",
        "salesquantity25q2"
    ],
    "Distribution": [
        "Distribution_source",
        "Distribution_cleaned"
    ]
}


def json_block_to_markdown_table(json_text: str) -> str:
    """Convert JSON array of dicts to Markdown table."""
    try:
        data = json.loads(json_text)
        if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
            return "⚠️ Invalid JSON structure."
        df = pd.DataFrame(data)

        preferred_order = [
            "Column Name", "Type", "Units", "Description",
            "Allowed Values / Range", "Missing %", "Cleaning / Notes"
        ]
        columns = [c for c in preferred_order if c in df.columns] + [
            c for c in df.columns if c not in preferred_order
        ]
        df = df[columns]
        return df.to_markdown(index=False)
    except Exception as e:
        return f"⚠️ Failed to convert JSON block: {e}"


def replace_json_blocks_with_tables(markdown_text: str) -> str:
    """Replace all ```json blocks with Markdown tables."""
    def replace_block(match):
        json_content = match.group(1).strip()
        return "\n" + json_block_to_markdown_table(json_content) + "\n"

    pattern = re.compile(r"```json\s*(.*?)\s*```", re.DOTALL)
    return pattern.sub(replace_block, markdown_text)


def clean_markdown_wrappers(text: str) -> str:
    """Remove ```markdown fenced blocks and duplicate top-level headers."""
    text = re.sub(r"^```markdown\s*", "", text.strip(), flags=re.DOTALL)
    text = re.sub(r"\s*```$", "", text.strip(), flags=re.DOTALL)
    # Remove redundant "Track & Trace Data Codebook" headers
    text = re.sub(r"^#\s*Track\s*&\s*Trace\s*Data\s*Codebook\s*", "", text, flags=re.IGNORECASE | re.MULTILINE)
    # Remove stray top-level headers like "# harvest"
    text = re.sub(r"^#\s*\w+\s*$", "", text, flags=re.MULTILINE)
    return text.strip()


def extract_table_name(text: str, fallback_name: str) -> str:
    """Extract table name from markdown content or filename."""
    match = re.search(r"Table:\s*([A-Za-z0-9_\-]+)", text)
    if match:
        return match.group(1).strip()
    return fallback_name


def find_category_for_file(table_name: str) -> str:
    """Return the category name for a given table name."""
    for category, files in files_by_folder.items():
        if table_name.lower() in [f.lower() for f in files]:
            return category
    return "Uncategorized"


def combine_markdown_codebooks(folder_path, output_filename="combined_codebook.md"):
    """Combine Markdown codebooks into one file grouped by category."""
    folder = Path(folder_path)
    output_path = folder / output_filename

    md_files = sorted(folder.glob("*_codebook_enhanced.md"))
    if not md_files:
        print("⚠️ No *_codebook_enhanced.md files found.")
        return

    print(f"📚 Found {len(md_files)} Markdown codebooks to combine.")
    combined_content = ["# Track & Trace Data Codebook\n"]

    # Store categorized data
    categorized_tables = {}

    for f in md_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        text = clean_markdown_wrappers(text)
        text = replace_json_blocks_with_tables(text)

        fallback_name = re.sub(r"_codebook_enhanced\.md$", "", f.name)
        table_name = extract_table_name(text, fallback_name)
        category = find_category_for_file(table_name)

        categorized_tables.setdefault(category, []).append((table_name, text))
        print(f"✅ Processed: {table_name} → {category}")

    # Build Table of Contents
    combined_content.append("## Combined Table Index\n")
    for category, tables in categorized_tables.items():
        combined_content.append(f"\n### {category}")
        for i, (table_name, _) in enumerate(tables, start=1):
            combined_content.append(f"- [Table: {table_name}](#table-{table_name.lower()})")
    combined_content.append("\n---\n")

    # Write tables grouped by category
    for category, tables in categorized_tables.items():
        combined_content.append(f"\n\n## {category}\n")
        for table_name, text in tables:
            separator = "\n" + ("=" * 80) + "\n"
            section_header = f"\n# Table: {table_name}\n"
            combined_content.append(separator)
            combined_content.append(section_header)
            combined_content.append(text.strip())
            combined_content.append("\n")

    # Save combined markdown
    output_path.write_text("\n".join(combined_content), encoding="utf-8")
    print(f"\n🎉 Combined codebook saved to: {output_path}")


# --------------------------------------------
# Example Usage
# --------------------------------------------
combine_markdown_codebooks("enhanced_codebooks")
