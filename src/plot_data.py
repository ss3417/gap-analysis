"""GDP visualisations."""
import matplotlib.pyplot as plt

def plot_gdp(df, output_path=None):
    """Plot GDP in current US dollars (trillions), returning fig and ax."""
    fig, ax = plt.subplots(figsize=(11, 6))
    for country, group in df.groupby("country"):
        ax.plot(group["year"], group["gdp_trillion_usd"], label=country, linewidth=2)
    ax.set(title="Annual GDP by country, 2000–2022", xlabel="Year", ylabel="GDP (current US$ trillions)")
    ax.legend(ncol=2)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, dpi=160, bbox_inches="tight")
    return fig, ax

def plot_indexed_gdp(df, output_path=None):
    """Compare GDP relative to each country's 2000 level (2000 = 100)."""
    fig, ax = plt.subplots(figsize=(11, 6))
    for country, group in df.groupby("country"):
        group = group.sort_values("year")
        base = group.loc[group["year"] == 2000, "gdp_usd"]
        if base.empty or base.iloc[0] <= 0:
            continue
        ax.plot(group["year"], 100 * group["gdp_usd"] / base.iloc[0], label=country, linewidth=2)
    ax.set(title="GDP indexed to 2000 = 100 (current US$)", xlabel="Year", ylabel="GDP index")
    ax.legend(ncol=2)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, dpi=160, bbox_inches="tight")
    return fig, ax
