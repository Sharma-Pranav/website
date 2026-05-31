---
draft: false
date: 2026-06-02
categories:
  - Notes
  - Forecasting
  - Decision Intelligence
tags:
  - forecasting
  - forecast-metrics
  - demand-planning
  - mae
  - bias
  - model-selection
---

# Which Forecast Metric Matters for Which Business Decision

Modern demand forecasting often optimizes for one metric, for example Mean Absolute Error.

This helps a lot in benchmarking, but it does not paint the complete picture needed to make trustworthy business decisions.

A metric like MAE is fundamental because it adds structure to model evaluation. Without it, comparing models becomes subjective. One person may prefer one model, another person may prefer another, and the discussion becomes opinion-based.

But one metric alone is not sufficient to guide replenishment, inventory planning, service levels, planner trust, and automation. These decisions do not fail in the same way. So one metric cannot explain the quality of the whole forecasting system.

Mean Absolute Error tells us how large the average error is.

In simple terms:

> If the forecast is wrong, how wrong is it on average?

That is useful. But it does not tell us whether the forecast is repeatedly too high or repeatedly too low.

This matters because both errors create different business problems.

Overforecasting may create excess inventory, blocked working capital, and waste.

Underforecasting may create stockouts, service issues, missed sales, and firefighting.

To address this, we also need to monitor bias.

But another question remains:

> What happens when the model is very wrong?

This is where tail metrics become important.

Tail metrics help us understand the worst failures of the model. If a few errors are very large, they can create huge operational imbalances and may require manual intervention. Over time, this can erode trust in the forecasting system.

Composite metrics can simplify comparison, but they can also hide the type of error the model is making.

That is why demand forecasting needs more than one metric.

We need metrics to select the right models.

We need metrics to protect inventory.

We need metrics to reduce service-level risk.

We need metrics to build planner trust.

And if the system is supposed to be automated, we also need metrics for monitoring, fallback logic, and deployment decisions.

This changes the view from one metric to multiple metrics that paint a more complete picture of the forecasting system.

Each metric helps the system see a different kind of risk.

That is what is required to make better business decisions with forecasts.
