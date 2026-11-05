from models import Product
from pydantic import ValidationError

test_cases = [
    {
        "data": {"name": "Laptop", "price": 15000, "stock": 5},
        "expected": "ACCEPTED"
    },
    {
        "data": {"name": "Mouse", "price": -100, "stock": 10},
        "expected": "REJECTED"
    },
    {
        "data": {"name": "Teclado", "price": 500, "stock": -2},
        "expected": "REJECTED"
    },
    {
        "data": {"name": "", "price": 200, "stock": 3},
        "expected": "REJECTED"
    },
    {
        "data": {"name": "   ", "price": 100, "stock": 5},
        "expected": "REJECTED"
    },
    {
        "data": {"name": "  Monitor  ", "price": 3000, "stock": 0},
        "expected": "ACCEPTED"
    }
]

for i, case in enumerate(test_cases, start=1):
    product = None
    error_message = ""

    try:
        product = Product(**case["data"])
        actual = "ACCEPTED"

    except ValidationError as error:
        actual = "REJECTED"
        error_message = error.errors()[0]["msg"]

    if actual == case["expected"]:
        if actual == "ACCEPTED":
            print(f"Test {i}: PASS - {actual} - {product}")
        else:
            print(f"Test {i}: PASS - {actual} - {error_message}")
    else:
        print(f"Test {i}: FAIL - Expected {case['expected']}, got {actual}")



