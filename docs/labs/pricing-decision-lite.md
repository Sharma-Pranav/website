# Pricing Decision Lite — Robust Price Selection Under Uncertainty

## Live demo (embedded)

<iframe
  src="https://pranavsharma-pricing-decision-lite.hf.space"
  style="width: 100%; height: 900px; border: 0; border-radius: 12px;"
  loading="lazy"
  allow="clipboard-read; clipboard-write"
></iframe>

- Open in new tab: <https://pranavsharma-pricing-decision-lite.hf.space>  
- Hugging Face page: <https://huggingface.co/spaces/PranavSharma/pricing-decision-lite>  
- GitHub repo: <https://github.com/Sharma-Pranav/pricing-decision-lite>  

---

## What you can do in the demo (30 seconds)

1. Choose a **data mode** (Synthetic vs observational-mode workflow).
2. Review the **profit distribution** across candidate prices.
3. See the **naïve optimum** vs the **robust (governed) recommendation**.
4. Inspect **downside risk** (e.g., low-quantile profit) and decision status:
   - **OPTIMIZE** (deploy a robust price)
   - **HOLD** (insufficient leverage / too fragile)
   - **NO-GO** (no feasible price meets governance)

---

## What this proves

- The price that maximizes expected profit is often **fragile under uncertainty**.
- **Downside-aware governance** changes decisions: it can shift the price or block deployment.
- Pricing decisions are **regime-conditional** (clean synthetic assumptions ≠ noisy observational reality).

---

## Decision logic (high level)

```mermaid
flowchart TD
  A[Inputs: price grid, cost, demand model] --> B[Bootstrap uncertainty<br/>elasticity + demand]
  B --> C[Profit distribution per price]
  C --> D{Governance checks<br/>downside quantiles + thresholds}
  D -->|Pass| E[OPTIMIZE<br/>choose robust price]
  D -->|Borderline| F[HOLD]
  D -->|Fail| G[NO-GO]
````

---

## Downloads

!!! info "Slides"

- [Direct download (PPTX)](https://raw.githubusercontent.com/Sharma-Pranav/pricing-decision-lite/main/Pricing_Decision_Lite%20%E2%80%94%20Robust_Price_Selection_Under_Uncertainty.pptx)
- [View on GitHub](https://github.com/Sharma-Pranav/pricing-decision-lite/blob/main/Pricing_Decision_Lite%20%E2%80%94%20Robust_Price_Selection_Under_Uncertainty.pptx)

---
