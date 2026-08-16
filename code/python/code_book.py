import os
import pandas as pd
import numpy as np
import json
from pathlib import Path
from google import genai

# ---------- Initialize client ----------
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ---------- Utility ----------
def clean_value(val):
    """Safely convert any value to a readable string or None."""
    if pd.isna(val):
        return None
    try:
        val_str = str(val).encode("utf-8", "ignore").decode("utf-8", "ignore").strip()
        if val_str.lower() in ["", "nan", "none"]:
            return None
        return val_str
    except Exception:
        return None

# ---------- Load Prompt ----------
PROMPT_TEMPLATE_PATH = Path("Track_Trace_Codebook_Prompt.txt")
if not PROMPT_TEMPLATE_PATH.exists():
    raise FileNotFoundError("❌ Missing Track_Trace_Codebook_Prompt.txt prompt file.")
PROMPT_TEMPLATE = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")

# ---------- Main Function ----------
def generate_codebooks_with_genai(input_path):
    input_path = Path(input_path)
    output_folder = input_path.parent / f"{input_path.name}_codebooks"
    output_folder.mkdir(exist_ok=True)

    # Load all tables
    if input_path.suffix in [".xlsx", ".xls"]:
        tables = pd.read_excel(input_path, sheet_name=None).items()
    elif input_path.is_dir():
        tables = [(f.stem, pd.read_csv(f)) for f in input_path.glob("*.csv")]
    else:
        raise ValueError("Please provide a folder of CSVs or an Excel workbook.")

    # ---------- Iterate ----------
    for name, df in tables:
        print(f"📘 Processing: {name}")

        # Drop unwanted "Unnamed:" columns
        unnamed_cols = [c for c in df.columns if str(c).startswith("Unnamed")]
        if unnamed_cols:
            print(f"⚙️ Dropping columns: {unnamed_cols}")
            df = df.drop(columns=unnamed_cols)

        # Build compact JSON summary
        summary = {
            "table_name": name,
            "num_rows": int(len(df)),
            "num_columns": int(df.shape[1]),
            "columns": []
        }

        for col in df.columns:
            col_data = df[col]
            dtype = str(col_data.dtype)
            missing_pct = float(col_data.isna().mean() * 100)
            example = clean_value(col_data.dropna().iloc[0]) if not col_data.dropna().empty else None

            col_info = {
                "name": col,
                "dtype": dtype,
                "missing_pct": round(missing_pct, 1),
                "example": example,
                "range": None,
                "anomalies": []
            }

            if np.issubdtype(col_data.dtype, np.number):
                min_val, max_val = float(col_data.min()), float(col_data.max())
                col_info["range"] = [min_val, max_val]
                if (col_data < 0).any():
                    col_info["anomalies"].append("negative values")
                if np.isinf(col_data).any():
                    col_info["anomalies"].append("infinite values")

            summary["columns"].append(col_info)

        # Convert to compact JSON string
        table_json = json.dumps(summary, ensure_ascii=False)

        # ---------- Call Gemini ----------
        print(f"🧠 Sending {name} to GenAI...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{PROMPT_TEMPLATE}\n\nJSON DATA:\n{table_json}",
            config={
                "temperature": 0.2  
            }
        )

        # Save response
        output_file = output_folder / f"{name}_codebook.txt"
        output_file.write_text(response.text, encoding="utf-8")
        print(f"✅ Saved: {output_file}")

    print(f"\n🎉 All table codebooks saved to: {output_folder}")

# ---------- Example Usage ----------
generate_codebooks_with_genai(r"Distribution")
