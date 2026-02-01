## Live demo (Hugging Face Space)

**Forecast Sandbox Lite — SKU Explorer (Streamlit)**

- **Open demo (new tab):** <https://pranavsharma-forecast-sandbox-lite.hf.space>  
- **Hugging Face Space page:** <https://huggingface.co/spaces/PranavSharma/Forecast-Sandbox-Lite>  
- **GitHub repo:** <https://github.com/Sharma-Pranav/forecast-sandbox-lite>  

### Embedded demo

<iframe
  src="https://pranavsharma-forecast-sandbox-lite.hf.space"
  style="width: 100%; height: 900px; border: 0; border-radius: 12px;"
  loading="lazy"
  allow="clipboard-read; clipboard-write"
></iframe>

### 30-second walkthrough

1. Pick a **SKU**.
2. See the **recommended model** and **Score = MAE + |Bias|**.
3. Check **demand regime** (ADI/CV² → Smooth / Erratic / Intermittent / Lumpy).
4. Compare **all models** (ranked table).
5. View **Actual vs Forecast** and download aligned CSV.

### What this demonstrates

- **No universal winner**: model performance depends on demand structure.
- **Win-rate is a trap**: portfolio loss is driven by tail errors.
- A **generalist fallback** reduces downside when structure is uncertain.

### Data powering the Space (precomputed artifacts)

- `data/processed/test.csv` — ground truth
- `metrics/best_models.csv` — per-SKU recommendation
- `metrics/combined_metrics.csv` — model comparison table
- `metrics/demand_profile.csv` — ADI/CV² regime tags
- `metrics/*_predictions.csv` — model forecasts

!!! info "Downloads"
    - [⬇️ Slides (PPTX)](https://raw.githubusercontent.com/Sharma-Pranav/forecast-sandbox-lite/main/Forecast_Sandbox__Regime_Aware_Model_Selection.pptx)
    - [View slides on GitHub](https://github.com/Sharma-Pranav/forecast-sandbox-lite/blob/main/Forecast_Sandbox__Regime_Aware_Model_Selection.pptx)

> The Space is intentionally a **viewer** for decision evidence (not a training environment).
