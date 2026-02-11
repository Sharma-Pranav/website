# Decision Kernel Lite — Choosing Under Uncertainty

Most decisions don’t fail because of bad math.  
They fail because uncertainty is handled informally.

Decision Kernel Lite makes that uncertainty explicit, compares options with clear risk lenses, and gives you a defensible recommendation you can actually explain.

---

## Try the live demo

-   [Open in new tab](https://pranavsharma-decision-kernel-lite.hf.space)
-   [Hugging Face Space](https://huggingface.co/spaces/PranavSharma/decision-kernel-lite)
-   [GitHub repository](https://github.com/Sharma-Pranav/decision-kernel-lite)

---

## What you can do in ~30 seconds

1.  Add **scenarios** and their **probabilities**  
    (if they don’t sum to 1, the app normalizes them)
2.  Add **actions** and **losses**  
    (loss matrix = action × scenario)
3.  Compare decisions through three lenses:
    -   **Expected Loss**
    -   **Minimax Regret**
    -   **CVaR** (tail risk)
4.  Copy the generated **Decision Card** for docs, memos, or slides

---

## Why this matters

In real teams:

-   probabilities are debated,
-   downside is often underestimated,
-   and rationales are written after the decision.

This tool flips that.  
It forces explicit assumptions **before** the decision and gives a traceable reason for the final choice.

---

## Core model

Every decision is represented as:

**Actions × Scenarios × Probabilities × Losses**

The kernel evaluates each action with multiple risk lenses and returns:

-   one recommended action,
-   side-by-side evidence,
-   and a plain-language rationale.

---

## The three decision lenses

### 1) Expected Loss

Use this when decisions are frequent and probabilities are reasonably trusted.  
It minimizes average long-run loss.

### 2) Minimax Regret

Use this when probabilities are contested or accountability is high.  
It minimizes worst-case hindsight regret.

### 3) CVaR (tail risk)

Use this when rare bad outcomes are unacceptable.  
It minimizes average loss in the worst tail of outcomes.

---

## How the app decides (high level)

```mermaid
flowchart TD  A[Inputs: Actions, Scenarios, Probabilities, Losses] --> B[Compute Expected Loss per action]  A --> C[Compute Regret matrix per action × scenario]  A --> D[Compute CVaR per action at alpha]  B --> E{Primary rule}  C --> E  D --> E  E -->|Expected Loss| F[Choose argmin Expected Loss]  E -->|Minimax Regret| G[Choose argmin Max Regret]  E -->|CVaR| H[Choose argmin CVaR]  F --> I[Decision Card]  G --> I  H --> I
```