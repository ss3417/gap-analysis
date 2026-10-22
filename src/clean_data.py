"""Validate and tidy GDP observations."""
import pandas as pd
from .load_data import COUNTRIES

def clean_gdp(df):
    """Return a sorted, long-form dataset with GDP in USD trillions."""
    required = {"country_code", "year", "gdp_usd"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")
    out = df.copy()
    out["year"] = pd.to_numeric(out["year"], errors="coerce")
    out["gdp_usd"] = pd.to_numeric(out["gdp_usd"], errors="coerce")
    out = out[out["country_code"].isin(COUNTRIES)].dropna(subset=["year", "gdp_usd"])
    out["year"] = out["year"].astype(int)
    out = out[out["year"].between(2000, 2022)].drop_duplicates(["country_code", "year"])
    out["country"] = out["country_code"].map(COUNTRIES)
    out["gdp_trillion_usd"] = out["gdp_usd"] / 1e12
    return out[["country", "year", "gdp_usd", "gdp_trillion_usd"]].sort_values(["country", "year"]).reset_index(drop=True)
