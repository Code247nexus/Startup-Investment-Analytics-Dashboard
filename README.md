# 🚀 Startup Investment Analytics Dashboard

An interactive **Streamlit dashboard** for analyzing startup investments, investor behavior, funding trends, investment stages, sectors, cities, and similar investors.

The project uses **Python, Pandas, Matplotlib, and Streamlit** to transform startup funding data into an interactive analytical dashboard.

---

## 📊 Project Overview

The **Startup Investment Analytics Dashboard** provides three major analysis modules:

### 1. Overall Analysis

Provides a high-level overview of the startup investment ecosystem:

- Total investment amount
- Maximum investment
- Average investment
- Number of funded startups
- Month-on-month investment trends
- Top sectors by investment amount
- Top sectors by number of startups
- Top funding rounds
- Funding amount by city
- Top startups year-wise
- Top startups overall
- Top investors by total investment

---

### 2. Investor Analysis

Select an investor to analyze their investment behavior.

The dashboard provides:

- Latest 5 investments
- Biggest investments by startup
- Sectors invested in
- Investment distribution by funding stage
- Investment distribution by city
- Year-wise investment trends
- Similar investors based on investment patterns

The **latest investments** are sorted by date so that the most recent investments appear first.

---

### 3. Startup Analysis

Select a startup to analyze its funding profile:

- Startup name
- Industry / vertical
- Sub-vertical
- Location
- Number of funding rounds
- Year-wise funding trend

---

## 🔍 Similar Investor Analysis

A key analytical feature of the project is finding investors with similar investment patterns.

The logic works in multiple stages:

```text
Selected Investor
       ↓
Find top investment sectors
       ↓
Calculate total investment in those sectors
       ↓
Create an investment range
       ↓
Find other investors investing in the same sectors
       ↓
Calculate their total investment
       ↓
Filter investors within the investment range
       ↓
Exclude the selected investor
       ↓
Display top similar investors
