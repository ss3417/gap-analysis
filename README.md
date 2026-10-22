# GDP analysis: 2000–2022

Modular Python project for annual GDP in the UK, US, Brazil, Japan, China, Germany and Switzerland.

## Data
World Bank indicator [NY.GDP.MKTP.CD](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD): GDP in **current US dollars** (not inflation-adjusted). The notebook downloads the data from the World Bank API, cleans it, and creates charts. An internet connection is required for the first download.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name gdp-analysis --display-name "Python (gdp-analysis)"
jupyter notebook
```
Open `notebooks/gdp_analysis.ipynb` and select the `Python (gdp-analysis)` kernel. Run all cells. Launch Jupyter from the repository root.

## Structure
- `src/load_data.py`: World Bank API loading
- `src/clean_data.py`: data validation and cleaning
- `src/plot_data.py`: plotting functions
- `notebooks/gdp_analysis.ipynb`: analysis and commentary
- `data/`: downloaded and cleaned CSV files (generated when notebook runs)
- `figures/`: generated plots

## Interpretation
Nominal US-dollar GDP combines changes in output, domestic prices and exchange rates. It should not be treated as real GDP growth. For real growth comparisons, use constant-price GDP or real GDP growth indicators instead.

## Git collaboration example
Create separate branches (`feature/load-data`, `feature/clean-data`, `feature/plots`, `feature/notebook`), assign one branch to each teammate, push to GitHub and merge each through a reviewed pull request. Avoid committing `.venv`.
