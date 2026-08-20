import pytest
from order_system import OrderManagement

def test_single_product_valid():
    items = [{"product_id": "P01", "quantity": 1, "unit_price": 1200.0, "discount": 0.0, "stock": 5}]
    res = OrderManagement.calculate_order(items, "SAVE10")
    assert res["shipping"] == 0.0
    assert res["coupon_discount"] == 120.0

def test_zero_or_negative_quantity():
    with pytest.raises(ValueError):
        OrderManagement.calculate_order([{"product_id": "P02", "quantity": 0, "unit_price": 100, "stock": 5}])

def test_out_of_stock():
    with pytest.raises(ValueError, match="out of stock"):
        OrderManagement.calculate_order([{"product_id": "P03", "quantity": 10, "unit_price": 100, "stock": 2}])

def test_invalid_coupon():
    with pytest.raises(ValueError, match="Invalid coupon"):
        items = [{"product_id": "P01", "quantity": 1, "unit_price": 500.0, "stock": 10}]
        OrderManagement.calculate_order(items, "WRONGCODE")

def test_free_shipping_threshold():
    items = [{"product_id": "P01", "quantity": 1, "unit_price": 400.0, "stock": 10}]
    res = OrderManagement.calculate_order(items)
    assert res["shipping"] == 50.0
