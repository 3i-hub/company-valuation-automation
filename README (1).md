# Multi-Ticker DCF Valuation

Automated Discounted Cash Flow (DCF) valuation for multiple companies using Python, Excel, and financial data. Generates Excel outputs and HTML reports, with offline fallback using preloaded FCF data. Can be hosted on GitHub Pages for live dashboards.

---

## Features

- Supports multiple tickers (default: AAPL, MSFT, TSLA, AMZN, GOOGL)
- Forecasts 5 years of Free Cash Flow (FCF)
- Calculates Enterprise Value and intrinsic value per share
- Generates Excel files with forecast and summary
- Generates HTML reports for each ticker
- Online data fetch via Yahoo Finance, offline fallback to CSV
- Compatible with GitHub Actions for automated updates

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/multi-ticker-dcf-valuation.git
cd multi-ticker-dcf-valuation
```

### 2. Install dependencies
```bash
pip install pandas numpy openpyxl yfinance
```

### 3. Place the CSV file
Ensure `data/multi_ticker_fcf.csv` exists (included in the repo).

### 4. Run the script
```bash
python scripts/run_dcf.py
```

---

## Output

1. **Excel files:** `data/valuations/{TICKER}_DCF.xlsx`  
   - `DCF` sheet: forecasted and discounted FCF  
   - `Summary` sheet: Enterprise Value, intrinsic value/share, growth rates

2. **HTML reports:** `reports/{TICKER}_DCF.html`  
   - View in browser for a quick summary of valuation metrics
   - Links to Excel outputs included

---

## Customization

- Tickers: modify `TICKERS` variable or set environment variable `DCF_TICKERS`
- Forecast years: change `YEARS` or `DCF_YEARS`
- Discount rate / terminal growth: adjust `DISCOUNT_RATE` / `TERMINAL_GROWTH` or use environment variables

---

## GitHub Pages (optional)

1. Copy all HTML reports to `docs/` folder
2. Go to repository **Settings → Pages**  
   - Branch: `main`  
   - Folder: `/docs`
3. Visit `<username>.github.io/<repo>` for live DCF reports

---

## Live DCF Reports

You can view all the DCF reports online via GitHub Pages:

- [AAPL Report](docs/AAPL_DCF.html)
- [MSFT Report](docs/MSFT_DCF.html)
- [TSLA Report](docs/TSLA_DCF.html)
- [AMZN Report](docs/AMZN_DCF.html)
- [GOOGL Report](docs/GOOGL_DCF.html)

> Note: Reports are updated automatically if you run `run_dcf.py` and copy outputs to `docs/`.

---

## License

MIT License © 2025 Indusri Gamidi
