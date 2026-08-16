# California Cannabis Market Concentration Analysis

**Project period:** 2025

Market concentration analysis of California's licensed cannabis retail and
cultivation markets, using the Herfindahl-Hirschman Index (HHI) to track whether
the market consolidated or stayed fragmented, by county and by parent company,
from 2018 through 2024.

## What this does

- Merges license registry data with retail sales and cultivation track-and-trace
  data, joined by county and rolled up to parent company.
- Calculates HHI at the state and county level, per-license and per-parent-company,
  to see where the market is concentrating over time.
- Runs the same pipeline in two implementations: an original Stata version
  (`code/stata/`) and a Python/Pandas port (`code/python/`, `notebooks/`) built to
  reproduce Stata's `collapse`, `merge`, and `tempfile` semantics exactly, so the
  two outputs reconcile.
- Visualizes county-level HHI trends over time with Matplotlib/Seaborn.

## Repository layout

| Path | Contents |
|---|---|
| `code/stata/` | Original Stata `.do` scripts: import/merge, concentration calculation |
| `code/python/` | Python/Pandas port of the same pipeline |
| `notebooks/` | Exploratory and visualization notebooks (cultivation, retail, distribution) |
| `results/` | Aggregated HHI outputs by county and statewide |
| `docs/codebooks/` | Data dictionaries for the underlying track-and-trace fields |

## Data sources

Built on the California Department of Cannabis Control's public license and
track-and-trace registries, plus a commercial market-intelligence license report.
The raw source files (multiple hundreds of MB per year) and the local Python
environment are excluded here for size; this repo carries the code, the
aggregated results, and the data dictionaries.

A separate, survey-based sub-study using human-subjects data collected under an
IRB-approved protocol exists outside this repo and is withheld per that study's
informed consent terms; it is not part of this analysis.

## Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter, Stata.
