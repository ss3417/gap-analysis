"""Download annual GDP data from the World Bank API."""
import requests
import pandas as pd

COUNTRIES = {"GBR":"United Kingdom", "USA":"United States", "BRA":"Brazil", "JPN":"Japan", "CHN":"China", "DEU":"Germany", "CHE":"Switzerland"}

def load_gdp(start=2000, end=2022):
    """Return annual GDP (current US dollars) for selected countries."""
    codes = ";".join(COUNTRIES)
    url = f"https://api.worldbank.org/v2/country/{codes}/indicator/NY.GDP.MKTP.CD"
    response = requests.get(url, params={"format":"json", "per_page":2000, "date":f"{start}:{end}"}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list) or len(payload) < 2 or payload[1] is None:
        raise ValueError(f"Unexpected World Bank response: {payload}")
    return pd.DataFrame([{"country_code":r["countryiso3code"], "year":r["date"], "gdp_usd":r["value"]} for r in payload[1]])
