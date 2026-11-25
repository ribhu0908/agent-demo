from expense_tracker import parse_amount, average, monthly_total, top_category


def test_parse_plain_amount():
    assert parse_amount("1250.5") == 1250.5


def test_parse_rupee_symbol():
    assert parse_amount("₹99") == 99.0


def test_average():
    assert average([100, 200, 300]) == 200


def test_top_category():
    expenses = [
        {"date": "2026-11-01", "amount": 300, "category": "food"},
        {"date": "2026-11-02", "amount": 100, "category": "travel"},
        {"date": "2026-11-03", "amount": 50, "category": "food"},
    ]
    assert top_category(expenses) == "food"
