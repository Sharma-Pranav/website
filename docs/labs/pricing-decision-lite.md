# Pricing Decision Lite — Robust Price Selection Under Uncertainty

Most pricing tools give you one “optimal” price.  
This demo asks a more practical question: **will that price still hold up when assumptions change?**

Pricing Decision Lite compares upside and downside, then gives a clear outcome:
**OPTIMIZE, HOLD, or NO-GO**.

---

## Try the live demo

<iframe
  src="https://pranavsharma-pricing-decision-lite.hf.space"
  style="width: 100%; height: 900px; border: 0; border-radius: 12px;"
  loading="lazy"
  allow="clipboard-read; clipboard-write"
></iframe>

- [Open in new tab](https://pranavsharma-pricing-decision-lite.hf.space)  
- [Hugging Face Space page](https://huggingface.co/spaces/PranavSharma/pricing-decision-lite)  
- [GitHub repository](https://github.com/Sharma-Pranav/pricing-decision-lite)

---

## What you can do in ~30 seconds

1. Choose a **data mode** (synthetic or observational-style workflow)
2. Review **profit distributions** across candidate prices
3. Compare the **naïve optimum** vs the **robust governed recommendation**
4. Inspect downside risk (for example, low-quantile profit) and final decision status:
   - **OPTIMIZE** — deploy a robust price
   - **HOLD** — signal is weak or fragile
   - **NO-GO** — no price passes governance criteria

---

## Why this matters

- The expected-profit-maximizing price can be fragile.
- Risk-aware governance often changes the final recommendation.
- Pricing is regime-dependent: clean synthetic assumptions and noisy observational settings can lead to very different conclusions.

This app is built for **decision quality under uncertainty**, not just point-estimate optimization.

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
