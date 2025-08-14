import os
import yfinance as yf
import pandas as pd
from datetime import datetime

TICKERS = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOGL"]

valuations_folder = "data/valuations"
reports_folder = "reports"
os.makedirs(valuations_folder, exist_ok=True)
os.makedirs(reports_folder, exist_ok=True)

def run_dcf(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5y")
    cashflow = stock.cashflow

    try:
        fcf = cashflow.loc["Total Cash From Operating Activities"] - cashflow.loc["Capital Expenditures"]
    except KeyError:
        print(f"Skipping {ticker} due to missing FCF data.")
        return

    fcf = fcf.dropna().astype(float)
    if len(fcf) < 2:
        print(f"Skipping {ticker} due to insufficient data.")
        return

    growth_rate = fcf.pct_change().mean()
    discount_rate = 0.08
    years = 5

    future_fcfs = [fcf.iloc[0] * (1 + growth_rate) ** i for i in range(1, years + 1)]
    discounted_fcfs = [fc / ((1 + discount_rate) ** i) for i, fc in enumerate(future_fcfs, start=1)]
    terminal_value = future_fcfs[-1] * (1 + 0.02) / (discount_rate - 0.02)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

    intrinsic_value = sum(discounted_fcfs) + discounted_terminal_value
    shares_outstanding = stock.info.get("sharesOutstanding", 1)
    intrinsic_value_per_share = intrinsic_value / shares_outstanding

    # Save Excel valuation
    df = pd.DataFrame({
        "Year": list(range(1, years + 1)),
        "Projected FCF": future_fcfs,
        "Discounted FCF": discounted_fcfs
    })
    df.to_excel(f"{valuations_folder}/{ticker}_DCF.xlsx", index=False)

    # Save HTML report
    html_report = f"""
    <html>
    <head><title>{ticker} DCF Valuation</title></head>
    <body>
    <h1>{ticker} DCF Valuation</h1>
    <p><b>Intrinsic Value per Share:</b> ${intrinsic_value_per_share:,.2f}</p>
    <p><b>Market Price:</b> ${hist['Close'][-1]:,.2f}</p>
    <p><b>Discount Rate:</b> {discount_rate*100}%</p>
    <p><b>Growth Rate:</b> {growth_rate*100:.2f}%</p>
    </body>
    </html>
    """
    with open(f"{reports_folder}/{ticker}_DCF.html", "w") as f:
        f.write(html_report)

if __name__ == "__main__":
    for t in TICKERS:
        run_dcf(t)
