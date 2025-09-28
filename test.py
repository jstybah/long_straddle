import yfinance as yf
import pandas as pd

tickers = ["SPY", "AAPL", "MSFT"]
dfs = []
for t in tickers:
    df = yf.download(t, period="5y", interval="1d", auto_adjust=False)
    df["ticker"] = t
    df = df.reset_index().rename(columns=str.lower)
    dfs.append(df)
bars = pd.concat(dfs, ignore_index=True)
# Save as parquet
bars.to_parquet("data/underlying_bars.parquet")

# Display the first few rows
print(bars.columns)