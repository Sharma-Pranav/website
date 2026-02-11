# Labs

These three labs are parts of the same bigger idea: **Forecast → Price → Decide**.

They are **not** one fully connected end-to-end pipeline yet.  
That is intentional.

Each step needs a different kind of dataset and assumptions, and I don’t currently have one public dataset that realistically supports all three steps at the same quality level.

So instead of forcing a fake “full cycle,” I built and validated each part properly.

---

## What this means in practice

- You can review each module on its own technical merits.
- You can see how the logic connects across the full decision cycle.
- You also get a clear boundary of what is done vs. what is next.

---

## Forecasting Sandbox (Lite)

This module focuses on **forecast quality and model governance** for SKU portfolios.

It benchmarks models, selects defensible per-SKU choices, and reports transparent evidence:
- **MAE**
- **Bias**
- **Score = MAE + |Bias|**
- regime tags (**ADI / CV²**)

→ [Open Forecasting Sandbox](forecasting-sandbox.md)

---

## Pricing Decision Lite

This module focuses on **pricing under uncertainty**, not fragile point estimates.

It produces:
- a clear decision state (**OPTIMIZE / HOLD / NO-GO**)
- a robust price recommendation
- profit distribution evidence across scenarios

→ [Open Pricing Decision Lite](pricing-decision-lite.md)

---

## Decision Kernel Lite

This module focuses on **final decision selection under risk**.

It makes assumptions explicit (actions, scenarios, probabilities, losses) and compares choices using:
- **Expected Loss**
- **Minimax Regret**
- **CVaR** (tail risk)

→ [Open Decision Kernel Lite](decision-kernel-lite.md)

---

## Current status

- **Today:** modular components are working and validated.
- **Next:** integrate into a single connected cycle when a suitable shared dataset is available.

---

## Scope

All labs here are independent portfolio work built with public/synthetic data where applicable.  
No confidential or proprietary employer information is included.
