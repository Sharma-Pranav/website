# Forecast Sandbox Lite — SKU Explorer

Most forecasting demos show one model and one accuracy number.  
This one is different: it helps you decide **which model to trust for each SKU**, based on demand behavior and transparent evidence.

---

## Try the live demo

- [Open demo (new tab)](https://pranavsharma-forecast-sandbox-lite.hf.space)  
- [Hugging Face Space page](https://huggingface.co/spaces/PranavSharma/Forecast-Sandbox-Lite)  
- [GitHub repository](https://github.com/Sharma-Pranav/forecast-sandbox-lite)

### Embedded demo

<iframe
  src="https://pranavsharma-forecast-sandbox-lite.hf.space"
  style="width: 100%; height: 900px; border: 0; border-radius: 12px;"
  loading="lazy"
  allow="clipboard-read; clipboard-write"
></iframe>

---

## What you can do in ~30 seconds

1. Select a **SKU**
2. See the **recommended model**
3. Review **Score = MAE + |Bias|**
4. Check demand regime via **ADI / CV²**  
   (Smooth / Erratic / Intermittent / Lumpy)
5. Compare all candidate models in a ranked table
6. View **Actual vs Forecast** and download aligned CSV output

---

## Why this matters

- There is no single model that wins for every SKU.
- Portfolio performance is often driven by tail mistakes, not average win-rate.
- When demand structure is unclear, a robust generalist fallback can reduce downside.

This app is built to support **defensible model choice**, not leaderboard chasing.

---

## What powers the demo

The Space runs on precomputed artifacts so it is fast, stable, and reproducible:

- `data/processed/test.csv` — ground truth
- `metrics/best_models.csv` — per-SKU recommendation
- `metrics/combined_metrics.csv` — model comparison table
- `metrics/demand_profile.csv` — ADI/CV² regime tags
- `metrics/*_predictions.csv` — model forecasts

---

## Download slides

!!! info "Slides"
    - [Direct download (PPTX)](https://raw.githubusercontent.com/Sharma-Pranav/forecast-sandbox-lite/main/Forecast_Sandbox__Regime_Aware_Model_Selection.pptx)
    - [View on GitHub](https://github.com/Sharma-Pranav/forecast-sandbox-lite/blob/main/Forecast_Sandbox__Regime_Aware_Model_Selection.pptx)

---

> This Space is intentionally a **decision-evidence viewer**, not a model-training environment.

## Scope note

This is an independent portfolio artifact.  
No proprietary or confidential employer information is included.
