import pytest
from product import format_product_info

def test_format_product_info():
    result = format_product_info(101, "Laptop", 5, 799.99)
    expected = (
        "Product Information:\n"
        "ID       : 101\n"
        "Name     : Laptop\n"
        "Quantity : 5\n"
        "Price    : $799.99"
    )
    assert result == expected

def test_format_product_info_with_different_values():
    result = format_product_info(202, "Smartphone", 10, 499.5)
    expected = (
        "Product Information:\n"
        "ID       : 202\n"
        "Name     : Smartphone\n"
        "Quantity : 10\n"
        "Price    : $499.50"
    )
    assert result == expected