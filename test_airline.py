import pytest
from app.airline_system import AirlineReservation

def test_successful_booking():
    airline = AirlineReservation()
    res = airline.book_seat("12A", "Alice", 15)
    assert res["status"] == "CONFIRMED"

def test_double_booking_error():
    airline = AirlineReservation()
    airline.book_seat("12A", "Alice", 15)
    with pytest.raises(ValueError, match="Seat already booked"):
        airline.book_seat("12A", "Bob", 15)

def test_cancellation_and_refund():
    airline = AirlineReservation()
    airline.book_seat("14B", "Charlie", 15)
    cancel_res = airline.cancel_seat("14B")
    assert cancel_res["status"] == "CANCELLED"
    assert cancel_res["refund_amount"] > 0
