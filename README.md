# Startup Investment Analytics Dashboard

An interactive Streamlit dashboard for analyzing startup investments, investor behavior, funding trends, investment stages, sectors, cities, and similar investors.

The project uses Python, pandas, Matplotlib, and Streamlit to transform startup funding data into an interactive analytical dashboard.

## Project Overview

The Startup Investment Analytics Dashboard provides three major analysis modules:

1. Overall Analysis
2. Investor Analysis
3. Startup Analysis

A key analytical feature of the dashboard is Similar Investor Analysis, which identifies investors with comparable investment patterns.

## 1. Overall Analysis

The Overall Analysis module provides a high-level overview of the startup investment ecosystem.

It includes:

- Total investment amount
- Maximum investment
- Average investment
- Number of funded startups
- Month-over-month investment trends
- Top sectors by investment amount
- Top sectors by number of startups
- Top funding rounds by amount
- Funding amount by city
- Top startups by year
- Top startups overall by total funding
- Top investors by total investment

## 2. Investor Analysis

The Investor Analysis module allows users to select an investor and analyze their investment behavior.

It provides:

- Latest five investments
- Largest startup investments
- Sectors invested in
- Investment distribution by funding stage
- Investment distribution by city
- Year-wise investment trends
- Similar investors based on investment patterns

The latest investments are sorted by date in descending order, ensuring that the most recent investments appear first.

## 3. Startup Analysis

The Startup Analysis module allows users to select a startup and analyze its funding profile.

It provides:

- Startup name
- Industry / vertical
- Sub-vertical
- Location
- Number of funding rounds
- Year-wise funding trend

## Similar Investor Analysis

Similar Investor Analysis is a key analytical feature of the project. It identifies investors with similar investment patterns using a multi-stage process.

The workflow is as follows:

1. Select an investor.
2. Identify the investor’s top investment sectors.
3. Calculate the selected investor’s total investment in those sectors.
4. Define an investment range.
5. Identify other investors investing in the same sectors.
6. Calculate their total investment.
7. Filter investors within the investment range.
8. Exclude the selected investor.
9. Display the top similar investors.

## Technology Stack

- Python
- pandas
- Matplotlib
- Streamlit
