# California Cannabis Market Concentration Analysis

Market concentration (Herfindahl-Hirschman Index) analysis of California's licensed
cannabis retail and cultivation markets, tracking concentration by county and by
parent company from 2018 to 2024.

## What this does

- Merges license registry data with retail sales and cultivation track-and-trace
  data by county and parent company.
- Calculates HHI (Herfindahl-Hirschman Index) at the state and county level, both
  per-license and rolled up to parent company, to see whether the market is
  consolidating or staying fragmented over time.
- Runs the same pipeline twice: an original Stata implementation (`code/stata/`)
  and a Python/Pandas port (`code/python/`, `notebooks/`) that reproduces Stata's
  `collapse`, `merge`, and `tempfile` semantics exactly, so results match between
  the two.
- Visualizes HHI trends by county with Matplotlib/Seaborn.

## Data sources

Built on California Department of Cannabis Control public license and
track-and-trace registries, plus a commercial market-intelligence license report.
The raw source files (multi-hundred-MB per year) and a working virtual environment
are excluded from this repo for size; only the code, small aggregated results
(`results/`), and data dictionaries (`docs/codebooks/`) are included.

A separate survey-based sub-study using human-subjects data collected under an
IRB-approved protocol exists outside this repo and is withheld per the terms of
that study's informed consent; it is not part of this analysis.

## Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter, Stata.
