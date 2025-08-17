
from pathlib import Path

SAMPLES = {
    "quarterly_report_acme_q2.txt": """
ACME CORP Q2 EARNINGS (Unaudited)
Revenue: $125M (+12% YoY)
Gross Margin: 54%
Operating Expenses: $48M
Operating Income: $19.5M
Net Income: $14.2M
Cash & Equivalents: $62M
Key Risks: FX volatility, input cost inflation.
Outlook: FY revenue growth 10-12%; margin expansion 100-150 bps.
""",

    "bank_10k_excerpt.txt": """
XYZ BANK ANNUAL REPORT EXCERPT
Net Interest Margin: 3.1%
Non-Performing Assets: 1.2%
CET1 Ratio: 12.8%
Liquidity Coverage Ratio: 126%
Risk Factors: Credit risk from SME portfolio, cyber security.
""",
}

def main():
    dst = Path(__file__).resolve().parents[1] / "data" / "docs"
    dst.mkdir(parents=True, exist_ok=True)
    for name, body in SAMPLES.items():
        (dst / name).write_text(body.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(SAMPLES)} sample docs to {dst}")

if __name__ == "__main__":
    main()
