"""Tiny expense tracker used to test the n8n coding agent.

It has 3 real bugs on purpose. Open them as GitHub issues (see ISSUES.md)
and let the agent fix them one by one.
"""
from datetime import datetime


def parse_amount(text):
    """'₹1,250.50' or '1250.5' -> 1250.5"""
    cleaned = text.replace("₹", "").strip()
    return float(cleaned)


def average(amounts):
    """Average of a list of amounts."""
    return sum(amounts) / len(amounts)


def monthly_total(expenses, month):
    """Sum of expenses in a month. month is 'YYYY-MM'.

    expenses: list of dicts like {"date": "2026-11-03", "amount": 120.0}
    """
    total = 0
    for e in expenses:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.strftime("%Y-%m") == month:
            total += e["amount"]
    return total


def top_category(expenses):
    """Category with the highest total spend."""
    totals = {}
    for e in expenses:
        cat = e.get("category", "other")
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return max(totals, key=totals.get)
